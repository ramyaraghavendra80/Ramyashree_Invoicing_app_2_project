from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser


class Invoices(models.Model):
    invoice_id = models.IntegerField()
    client_name = models.CharField(max_length=250)
    date = models.DateField()
    
class Item(models.Model):
    invoice=models.ForeignKey(Invoices, on_delete=models.CASCADE,blank=True,null=True,related_name='items')
    desc=models.CharField(max_length=250)
    rate=models.FloatField()
    quantity=models.IntegerField()

class UserManager(BaseUserManager):
    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("Username should be provided")
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setddefault('is_superuser',True)
        return self.create_user(username,password,**extra_fields)

class User(AbstractBaseUser):
    id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=100)
    email_id= models.EmailField(max_length=200,unique=True)
    password=models.CharField(max_length=16)
    username=models.CharField(max_length=100, unique=True)

    USERNAME_FIELD='username'

    objects=UserManager()
