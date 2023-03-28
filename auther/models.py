from django.db import models

models.DateField()

class StudentForm(models.Model):  
    firstname = models.CharField("Enter first name", max_length=50)  
    lastname  = models.CharField("Enter last name", max_length = 50)  
    email     = models.EmailField("Enter Email")  
    file      = models.FileField() # for creating file input  
   
    class Meta:  
        db_table = "student"

created_at= models.DateField(auto_now_add=True)
updated_at =models.DateField(auto_now  = True)


# class Invoice(models.Model):
#     invoice_number = models.CharField(max_length=20)
#     date = models.DateField()
#     client_name = models.CharField(max_length=100)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

class Invoice(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=20)
    invoice_date = models.DateField()
    invoice_number = models.CharField(max_length=20)


# myapp/models.py

from django.db import models

class Organization(models.Model):
    OrgID = models.IntegerField(primary_key=True)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    Phone = models.CharField(max_length=12)
    CIN = models.CharField(max_length=10)
    PAN = models.CharField(max_length=10)
    TAN = models.CharField(max_length=10)
    DisplayName = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    CreateDate = models.DateField()
    Active = models.BooleanField(default=True)
    WebUrl = models.URLField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    PIN = models.IntegerField()

# myapp/forms.py

from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        db_table = 'db.auther_organization'
        fields = '__all__'
