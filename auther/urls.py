
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
    path('upload', views.upload, name='upload'),


]