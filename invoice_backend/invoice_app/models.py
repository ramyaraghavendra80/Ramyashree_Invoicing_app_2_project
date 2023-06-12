from django.db import models

class Invoices(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=250)
    date = models.DateField()
    
class Item(models.Model):
    desc=models.CharField(max_length=250)
    rate=models.DecimalField(max_digits=6,decimal_places=2)
    quantity=models.DecimalField(max_digits=4,decimal_places=2)

class User(models.Model):
    user_id=models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250, unique=True)
    email_id=models.CharField(max_length=250, unique=True)
    password=models.CharField(max_length=100)
