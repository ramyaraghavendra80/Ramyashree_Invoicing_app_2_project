from django.shortcuts import render
from django.views import View
from django.http import JsonResponse, Http404, HttpResponseBadRequest
from .serializers import *
from .data import *
import json
import uuid

# Create your views here.

class Invoices(View):
    def get(self,request):
        return JsonResponse(invoicedata, safe=False)

    def post(self,request):
        invoice_data=json.loads(request.body)
        invoice_data["invoice_id"]=len(invoicedata)+1
        invoice_serialized=InvoicesSerializer(data=invoice_data)
        if(invoice_serialized.is_valid()):
            invoicedata.append(invoice_serialized.data)

            return JsonResponse(invoice_serialized.data, safe=False)
        else:
            return JsonResponse(invoice_serialized.errors, safe=False)

class Invoice_detail(View):
    def get(self,request,invoice_id):
        invoice=next((invoice for invoice in invoicedata if invoice['invoice_id']== invoice_id), None)
        return JsonResponse(invoice,safe=False)

class Add_Item(View):
    def post(self,request,invoice_id):
        item_data=json.loads(request.body)
        item_serialized=ItemSerializer(data=item_data)
        if(item_serialized.is_valid()):
            for item in invoicedata:
                if item["invoice_id"]==invoice_id:
                    item["items"].append(item_serialized.data)
                return JsonResponse(item_serialized.data, safe=False)
            return JsonResponse(item_serialized.errors, safe=False)

class UserSignup(View):
    def post(self, request):
        user_data=json.loads(request.body)
        user_data["user_id"]=len(userdata)+1
        user_serialized=UserSerializer(data=user_data)
        if(user_serialized.is_valid()):
            userdata.append(user_serialized.data)
            return JsonResponse({"message":"Registered successfully", "state":True})
        return JsonResponse({"message":"Registration not successfull","state":False})

class UserSignin(View):
    def post(self, request):
        user_data=json.loads(request.body)
        print(user_data)
        print(user_data["email_id"])
        for info in userdata:
                if(info["email_id"]==user_data["email_id"] and info["password"]==user_data["password"]):
                    token=str(uuid.uuid4())
                    return JsonResponse({"token":token,"message":"Login done","state":True})
        return JsonResponse({"message":"login not successfull","state":False})
