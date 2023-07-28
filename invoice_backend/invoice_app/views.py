from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from .serializers import *
from .data import *
import json
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class Invoice(APIView):
    def get(self,request):
        invoicedata= Invoices.objects.all()
        serializer = InvoicesSerializer(invoicedata,many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data=json.loads(request.body)
        serializer=InvoicesSerializer(data=data)
        if serializer.is_valid():
            Invoices.objects.create(**serializer.data)
            return JsonResponse(data,status=200,safe=False)
        return JsonResponse(serializer.errors,status=201,safe=False)

class Invoice_detail(APIView):
    def get(self, request, invoice_id):
        invoice = Invoices.objects.filter(id=invoice_id).first()
        print(invoice)
        if invoice:
            item = Item.objects.filter(invoice=invoice.id).values()
            serializer = InvoicesSerializer(invoice).data
            serializer["item"]=list(item)
            return JsonResponse(serializer,status=200,safe=False)
        return JsonResponse({"message":"Inovice Not Found"})

class Add_Item(APIView):
    def post(self, request, invoice_id):
        invoice_data=json.loads(request.body)
        invoice_data["invoice"]=invoice_id
        serializer=ItemSerializer(data=invoice_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(invoice_data,status=200,safe=False)
        return JsonResponse(serializer.errors,status=201,safe=False)

class SignUp(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return JsonResponse(
                {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                }
                )
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
class SignIn(APIView):
    def post(self,request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh =RefreshToken.for_user(user)
            return JsonResponse(
                {
                    'refresh':str(refresh),
                    'access':str(refresh.access_token),
                }
            )
        return JsonResponse(serializer.errors, safe=False)
