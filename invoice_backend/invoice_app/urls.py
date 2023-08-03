from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('user/signup/',SignUp.as_view(), name="user_signup"),
    path('user/login/', SignIn.as_view(), name="user_signin"),
    path('invoices/', Invoice.as_view(), name="invoices"),
    path('invoices/new_invoice/', Invoice.as_view(), name="new_invoices"),
    path('invoices/<int:invoice_id>/', Invoice_detail.as_view(), name="invoices"),
    path('invoices/<int:invoice_id>/items/', Add_Item.as_view(), name="item"),

]