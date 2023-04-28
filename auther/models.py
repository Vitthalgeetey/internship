from django.db import models
from django import forms
# from .models import Organization
from django.utils.timezone import now
import datetime
models.DateField()


#------------------ Organization form -----------

class Organization(models.Model):
    Id = models.AutoField(primary_key=True)
    Email = models.EmailField()
    Address = models.CharField(max_length=100)
    Phone = models.CharField(max_length=12)
    CIN = models.CharField(max_length=10)
    PAN = models.CharField(max_length=10)
    TAN = models.CharField(max_length=10)
    DisplayName = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    CreateDate = models.DateTimeField(auto_now_add=True,null=True)
    Active = models.BooleanField(default=True)
    WebUrl = models.URLField()
    City = models.CharField(max_length=50)
    State = models.CharField(max_length=50)
    Country = models.CharField(max_length=50)
    PIN = models.IntegerField()
    
    def __str__(self):
        return self.Name



class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        db_table = 'db.auther_organization'
        fields = '__all__'

class template(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Type = models.CharField(max_length=10)
    OrgFK = models.ForeignKey(Organization, on_delete=models.CASCADE)
    Path = models.CharField(max_length=200)
    Default = models.BooleanField(default=False)

    def __str__(self):
        return self.Name


# ------------- Invoice --------------------




#------------------ Company form -----------
class company(models.Model):
    Id= models.AutoField(primary_key=True)
    Address = models.CharField(max_length=100)
    PAN = models.CharField(max_length=10)
    GST = models.CharField(max_length=10)
    Name = models.CharField(max_length=100)

    def __str__(self):
        return self.Name

class item(models.Model):
 Id=models.AutoField(primary_key=True)
 Name=models.CharField(max_length=100)
 Description=models.CharField(max_length=100)
 Value=models.CharField(max_length=100)
 ValueType=models.CharField(max_length=100)
 GST=models.IntegerField()
 SSN=models.IntegerField()
 HSN=models.IntegerField()
 TANType=models.CharField(max_length=100)

 def __str__(self):
        return self.Name


class templatefields(models.Model):
    Id= models.AutoField(primary_key=True)
    TemplateIdfk1 =models.ForeignKey(template, on_delete=models.CASCADE)
    FieldName= models.CharField(max_length=10)
    FieldType = models.CharField(max_length=10)
    Validation = models.CharField(max_length=100)

    def __str__(self):
        return self.Name
 


class companyForm(forms.ModelForm):
    class Meta:
        model = company
        db_table = 'db.auther_invoice'
        fields = '__all__'



#------------------ bank form -----------
class bank(models.Model):
    Id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    AccNo = models.CharField(max_length=10)
    IFSC = models.CharField(max_length=100)
    SWIFT = models.CharField(max_length=100)
    OrgFk2 = models.ForeignKey(Organization, on_delete=models.CASCADE)
    City = models.CharField(max_length=100)

    def __str__(self):
        return self.Name



class bankForm(forms.ModelForm):
    class Meta:
        model = bank
        db_table = 'db.auther_invoice'
        fields = '__all__'



    #------------GenerateInvoice-------

class generateinvoice(models.Model):
    Id=models.AutoField(primary_key=True)
    CustomerName = models.CharField(max_length=100)
    Date = models.DateField()
    TotalAmount = models.DecimalField(max_digits=8, decimal_places=2)
    InvoiceNumber=models.IntegerField()

    def __str__(self):
        return self.Name

class invoice(models.Model):

    Id = models.AutoField(primary_key=True)
    InvoiceNumber = models.CharField(max_length=255)
    InvoiceDate = models.DateField()
    GeneratedFor = models.CharField(max_length=255)
    TemplateIdfk =  models.ForeignKey(template, on_delete=models.CASCADE)
    CurrencyType = models.CharField(max_length=10)
    bankfk =  models.ForeignKey(bank, on_delete=models.CASCADE)
    ItemFK =  models.ForeignKey(item, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name


class invoiceform(forms.ModelForm):
    class Meta:
        model = invoice
        db_table = 'db.auther_invoice'
        fields = '__all__'


class templateform(forms.ModelForm):
    class Meta:
        model = template
        db_table = 'db.auther_invoice'
        fields = '__all__'

class itemform(forms.ModelForm):
    class Meta:
        model = item
        db_table = 'db.auther_item'
        fields = '__all__'

class templatefieldsform(forms.ModelForm):
    class Meta:
        model = templatefields
        db_table = 'db.auther_templatefields'
        fields = '__all__'

class Generateinvoiceform(forms.ModelForm):
    class Meta:
        model = generateinvoice
        db_table = 'db.auther_generateinvoice'
        fields = '__all__'



        

