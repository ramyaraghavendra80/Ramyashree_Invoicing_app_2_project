from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt


urlpatterns=[
    path('user/signup/', csrf_exempt(SignUp.as_view()), name="user_signup"),
    path('user/login/', csrf_exempt(SignIn.as_view()), name="user_signin"),
    path('invoices/', csrf_exempt(Invoice.as_view()), name="invoices"),
    path('invoices/new_invoice/', csrf_exempt(Invoice.as_view()), name="new_invoices"),
    path('invoices/<int:invoice_id>/', csrf_exempt(Invoice_detail.as_view()), name="invoices"),
    path('invoices/<int:invoice_id>/items/', csrf_exempt(Add_Item.as_view()), name="item"),

]