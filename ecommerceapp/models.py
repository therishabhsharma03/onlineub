from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from datetime import time
from django import forms

# Create your models here.
class Contact(models.Model):
    contact_id=models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email=models.EmailField()
    desc = models.TextField(max_length=100)
    phonenumber=models.IntegerField()

    def __str__(self):
        return  self.name

class Menu(models.Model):
    product_id=models.AutoField
    product_name=models.CharField(max_length=100)
    category = models.CharField(max_length=100,default="")
    subcategory = models.CharField(max_length=50,default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media/images',default="")
    
  
    def __str__(self):
        return self.product_name

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null =True)

    def __str__(self):
        return self.name

class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json =  models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=90)
    block= models.CharField(max_length=200)
    room_num = models.CharField(max_length=200)
    reg = models.CharField(max_length=200, default="")
    
    oid=models.CharField(max_length=150,blank=True)
    amountpaid=models.CharField(max_length=500,blank=True,null=True)
    paymentstatus=models.CharField(max_length=20,blank=True)
    phone = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.name 



class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    delivered=models.BooleanField(default=False)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."