
from django.urls import path,include
from . import views

urlpatterns = [



    path('',views.home,name='home'),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signout',views.signout,name='signout'),
    
    # path('invoice',views.invoice1,name='invoice'),
    # path('invoice',views.invoice1,name='invoice'),
    # path('sample',views.sample,name='sample'),
   
    # path('temp1', views.temp1, name='temp1'),
    # path('temp2', views.temp2, name='temp2'),

    path('succ', views.success, name='succ'),
    path('org', views.organization_form, name='org'),
    path('invoice', views.invoice, name='invoice'),

    path('company', views.company_form, name='company'),
    path('item', views.item_form, name='item'),
    path('templatefields', views.templatefields_form, name='templatefields'),
    path('bank', views.bank_form, name='bank'),
    path('template', views.template_form, name='template'),


    

    path('contact', views.contact, name='contact'),
    path('About', views.About, name='About'),


]











    # path('sample',views.sample,name='sample'),
   
    # path('temp1', views.temp1, name='temp1'),
    # path('temp2', views.temp2, name='temp2'),
