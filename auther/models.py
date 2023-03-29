from django.db import models
from django import forms

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

class invoice(models.Model):

    Id = models.AutoField(primary_key=True)
    InvoiceNumber = models.CharField(max_length=255)
    InvoiceDate = models.DateField()
    GeneratedFor = models.CharField(max_length=255)
    TemplateIdfk = models.IntegerField()
    CurrencyType = models.CharField(max_length=10)
    Bank = models.CharField(max_length=255)
    itemfk = models.IntegerField()


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        db_table = 'db.auther_organization'
        fields = '__all__'

class invoiceform(forms.ModelForm):
    class Meta:
        model = invoice
        db_table = 'db.auther_invoice'
        fields = '__all__'
