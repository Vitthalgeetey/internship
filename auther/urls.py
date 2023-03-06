
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    path('invoice',views.invoice1,name='invoice'),
    path('sample',views.sample,name='sample'),
    path('upload', views.upload, name='upload'),
    path('temp1', views.temp1, name='temp1'),
    path('temp2', views.temp2, name='temp2'),
    path('form', views.form, name='form'),

    path('contact', views.contact, name='contact'),
    path('About', views.About, name='About'),
    path('Invoice', views.generate_invoice, name='Invoice'),


]