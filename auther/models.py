from django.db import models

models.DateField()

class StudentForm(models.Model):  
    firstname = models.CharField("Enter first name", max_length=50)  
    lastname  = models.CharField("Enter last name", max_length = 50)  
    email     = models.EmailField("Enter Email")  
    file      = models.FileField() # for creating file input  
   
    class Meta:  
        db_table = "student"

created_at= models.DateField(auto_now_add=True)
updated_at =models.DateField(auto_now  = True)


class Invoice(models.Model):
    invoice_number = models.CharField(max_length=20)
    date = models.DateField()
    client_name = models.CharField(max_length=100)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
