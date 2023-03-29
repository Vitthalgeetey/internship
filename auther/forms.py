from django import forms  

from .models import company
from .models import Organization

# ----------org form-----------------
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['OrgID','Email', 'Address', 'Phone', 'CIN', 'PAN', 'TAN', 'DisplayName', 'Name', 'CreateDate', 'Active', 'WebUrl', 'City', 'State', 'Country', 'PIN']
      

# -----------company form--------------
class companyForm(forms.ModelForm):
    class Meta:
        model = company
        fields = ['CompanyID', 'Address','PAN','Name','GST']

