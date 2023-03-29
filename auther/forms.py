from django import forms  


from .models import Organization
from .models import invoice    

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['OrgID','Email', 'Address', 'Phone', 'CIN', 'PAN', 'TAN', 'DisplayName', 'Name', 'CreateDate', 'Active', 'WebUrl', 'City', 'State', 'Country', 'PIN']
      

class invoiceform(forms.ModelForm):
    class Meta:
        model = invoice
        fields = ['Id','InvoiceNumber','InvoiceDate','GeneratedFor','TemplateIdfk','CurrencyType','Bank','itemfk']
      

