from django import forms  
# import datetime 
from auther.models import StudentForm  #models.py
# from .models import Invoice

from .models import Organization


# from .models import Post
class StudentForm(forms.ModelForm):  
    class Meta:  
        model = StudentForm  
        fields = "__all__"
 
    def __init__(self, *args, **kwargs):
            super(StudentForm, self).__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                field.widget.attrs['class'] = 'form-control'   
                
class dateinput(forms.DateInput):
     input_type = 'date'
# class org(forms.ModelForm):
#     class Meta:
#         model = Post
#         fields = [Email, Adress, phone, CIN, PAN, TAN, DispayDate, Name, CreateDate,  Active,  WebUrl, city,  state , Country,  Adress ]


class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['OrgID','Email', 'Address', 'Phone', 'CIN', 'PAN', 'TAN', 'DisplayName', 'Name', 'CreateDate', 'Active', 'WebUrl', 'City', 'State', 'Country', 'PIN']
      

