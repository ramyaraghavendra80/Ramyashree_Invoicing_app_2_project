from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from .serializers import *
from .data import *
import json
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
# Create your views here.

class Invoice(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self,request):
        invoicedata= Invoices.objects.filter(user=request.user.id)
        serializer = InvoicesSerializer(invoicedata,many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data=json.loads(request.body)
        data["user"]=request.user.id
        serializer=InvoicesSerializer(data=data)
        if serializer.is_valid():
            # Invoices.objects.create(**serializer.data)
            serializer.save() 
            return JsonResponse({"message":"Inovice created"},status=200,safe=False)
        return JsonResponse(serializer.errors,status=201,safe=False)

class Invoice_detail(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request, invoice_id):
        invoice = Invoices.objects.get(user=request.user.id,invoice_id=invoice_id)
        if invoice:
            serializer = InvoicesSerializer(invoice).data
            return JsonResponse(serializer,status=200,safe=False)
        return JsonResponse({"message":"Inovice Not Found"})

class Add_Item(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, invoice_id):
        invoice_data=json.loads(request.body)
        invoice_data["invoice"]=invoice_id
        serializer=ItemSerializer(data=invoice_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"message":"Item added to Inovice"})
        return JsonResponse(serializer.errors,status=201,safe=False)

class SignUp(APIView):
    def post(self,request):
        data=json.loads(request.body)
        userExist = User.objects.filter(email_id=data["email_id"])
        if not userExist:
            serializer = UserSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Signup successful"},status=status.HTTP_201_CREATED)
            return JsonResponse(serializer.errors, safe=False)
        return JsonResponse({"message": "uaer account exist"})


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
