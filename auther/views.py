from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.http import HttpResponse



from .models import Invoice

from django.shortcuts import render
from .forms import InvoiceForm

def Invoice1(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            # Process form data here
            model_instance = form.save(commit=False)
            model_instance.save()
            print("Succesfull")
            return HttpResponse("File uploaded successfuly")  
    else:
        form = InvoiceForm()
    return render(request, 'auther/Invoice1.html', {'form': form})



   







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
def invoice1(request):
    return render(request,'auther/invoice.html')
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

def signin(request):
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

        return render(request,'auther/signin.html')

def signout(request):
    logout(request)
    messages.success(request,"logged out successfully")
    return redirect('home')

    

