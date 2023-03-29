from django import forms  


from .models import company
from .models import Organization
from .models import bank
from .models import template
from .models import invoice

# ----------org form-----------------


from .models import Organization
from .models import invoice   
from .models import item 
from .models import templatefields


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['OrgID','Email', 'Address', 'Phone', 'CIN', 'PAN', 'TAN', 'DisplayName', 'Name', 'CreateDate', 'Active', 'WebUrl', 'City', 'State', 'Country', 'PIN']
      

# -----------company form--------------
class companyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['Id', 'Address','PAN','Name','GST']

#--------------invoice form ------------
class invoiceform(forms.ModelForm):
    class Meta:
        model = invoice
        fields = ['Id','InvoiceNumber','InvoiceDate','GeneratedFor','TemplateIdfk','CurrencyType','Bank','itemfk']

#---------------item-----------
class itemform(forms.ModelForm):
    class Meta:
        model = item
        fields =['Id','Name','Description','Value','ValueType','GST','SSN','HSN','TANType']

#---------templatefields---------

class templatefieldsform(forms.ModelForm):
    class Meta:
        model = templatefields
        fields =['Id','TemplateIdfk1','FieldName','FieldType','Validation']
class bankform(forms.ModelForm):
    class Meta:
        model = bank
        fields = ['ID', 'Name', 'AccNo', 'IFSC', 'SWIFT', 'ORGFK2']

class templateform(forms.ModelForm):
    class Meta:
        model = template
        fields = ['TemplateID','Name','Type','OrgFK','Path', 'Default']
       

