from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.db import connection
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import OrganizationForm
from .forms import companyForm
from .forms import itemform
from .forms import templatefieldsform
from .forms import bankform
from .forms import templateform
from .forms import Generateinvoiceform
from django.apps import apps
from django.forms.models import modelform_factory
from django.forms import ModelChoiceField


def Generateinvoice_form(request):
    if request.method == 'POST':
        form = Generateinvoiceform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return HttpResponse("success")
    else:
        form = OrganizationForm()

    return render(request, 'auther/Generateinvoice.html', {'form': form})




#-------------org form ---------------------------
from django.shortcuts import render, redirect
from .forms import OrganizationForm
from .forms import invoiceform

def organization_form(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = OrganizationForm()
    return render(request, 'auther/organization_form.html', {'form': form})


def success(request):
    return render(request, 'auther/success.html')



#---------------company form------------------------
def company_form(request):
    if request.method == 'POST':
        form = companyForm(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = companyForm()
    return render(request, 'auther/company_form.html', {'form': form})

#---------Item Form----------------

def item_form(request):
    if request.method == 'POST':
        form = itemform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = itemform()
    return render(request, 'auther/item_form.html', {'form': form})

#---------templatefields------------
def templatefields_form(request):
    if request.method == 'POST':
        form = templatefieldsform(request.POST)
        if form.is_valid():
            form.save()
        
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = templatefieldsform()
    return render(request, 'auther/templatefields_form.html', {'form': form})


# ==========Invoice Form ============

def invoice(request):
    if request.method == 'POST':
        form = invoiceform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = invoiceform()
    return render(request, 'auther/invoice_form.html', {'form': form})




#---------------bank form------------------------
def bank_form(request):
    if request.method == 'POST':
        form = bankform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = bankform()
    return render(request, 'auther/bank_form.html', {'form': form})



#---------------template form------------------------
def template_form(request):
    if request.method == 'POST':
        form = templateform(request.POST)
        if form.is_valid():
            form.save()
            # return redirect('success')
            return render(request, 'auther/success.html')
    else:
        form = templateform()
    return render(request, 'auther/template_form.html', {'form': form})

def show_template(request, table_name, model_name, app_name):
    with connection.cursor() as cursor:
        cursor.execute(f"SELECT * FROM {table_name} LIMIT 1")
        columns = [col[0] for col in cursor.description]
        cursor.execute(f"SELECT * FROM {table_name}")
        rows = cursor.fetchall()
    return render(request, 'auther/show.html', {'table_name': table_name,'model_name': model_name, 'app_name': app_name, 'columns': columns, 'rows': rows})

def delete_row(request, table_name, app_name, model_name, row_id):
    with connection.cursor() as cursor:
        cursor.execute(f"DELETE FROM {table_name} WHERE Id=%s", [row_id])
    messages.success(request,"the template has been deleted successfully")
    return redirect('show_template',table_name=table_name , model_name=model_name, app_name=app_name)




def update_row(request, table_name, app_name, model_name, row_id):

    model_class = apps.get_model(app_name, model_name)

    columns = [field.name for field in model_class._meta.fields]

    class CustomFormClass(modelform_factory(model_class, fields=columns)):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            for field_name, field in self.fields.items():
                if isinstance(field, ModelChoiceField):
                    related_model = field.queryset.model
                    related_objects = related_model.objects.all()
                    self.fields[field_name] = ModelChoiceField(queryset=related_objects)

    # Get the row to update
    row = model_class.objects.filter(Id=row_id).first()

    # If the row doesn't exist, redirect to an error page
    if not row:
        return redirect('error')

    # If the request method is POST, update the row and redirect to the updated row's page
    if request.method == 'POST':
        form = CustomFormClass(request.POST, instance=row)
        if form.is_valid():
            form.save()
            return redirect('show_template',table_name=table_name , model_name=model_name, app_name=app_name)


    # If the request method is GET, render the update form
    else:
        form = CustomFormClass(instance=row)

    return render(request, 'auther/update_row.html', {'app_name': app_name, 'model_name': model_name, 'form': form})









# ----------------
def form(request):
    return render(request,'auther/form.html')
def temp2(request):
    return render(request,'auther/temp2.html')
def temp1(request):
    return render(request,'auther/temp1.html')
def About(request):
    return render(request,'auther/About.html')
def contact(request):
    return render(request,'auther/contact.html')
# def invoice1(request):
#     return render(request,'auther/invoice.html')
def home(request):
    return render(request,'auther/index.html')

def sample(request):
    return render(request,'auther/sample.html')

def signup(request):
    print("Sign up")
    if request.method == 'POST':
        username= request.POST['username']
        fname= request.POST['fname']
        lname= request.POST['lname']
        email= request.POST['email']
        pass1= request.POST['pass1']
        pass2= request.POST['pass2']

        #validations

        if User.objects.filter(username=username):
            messages.error(request,"Username already exist!")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request,"Email already exist!")
            return redirect('home')

        if len(username)>10:
            messages.error(request,"Username must be under 10 characters")
            return redirect('home')

        if pass1!=pass2 :
            messages.error(request,"Password didn't match")
            return redirect('home')

        if not username.isalnum():
            messages.error(request,"Username must be Alpha-numeric!")
            return redirect('home')

        myuser= User.objects.create_user(username,email,pass1)
        myuser.first_name= fname
        myuser.last_name= lname 
        myuser.save()
        messages.success(request,"your account has been created successfully")
        return redirect('signin')

    return render(request,'auther/signup.html')

def Login(request):
        if request.method == "POST":
            username=request.POST['username']
            pass1=request.POST['pass1']
            user=authenticate(username=username,password=pass1)
            if user is not None:
                login(request,user)
                fname=user.first_name
                return render(request,'auther/index.html',{'fname':fname})
            else:
                messages.error(request,"bad credentials")
                return redirect('home')

        return render(request,'auther/Login.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')

    

