from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)  # Assuming a phone number won't exceed 20 characters

    class Meta:
        db_table = "Register"

class contactus(models.Model):
    firstname = models.TextField(max_length=255)
    lastname =models.TextField(max_length=255)
    email = models.EmailField(primary_key=True)
    comment= models.TextField(max_length=255)

    class Meta:
        db_table = "contactus"

from django.db import models

# Create your models here.
class URL(models.Model):
    long_url=models.URLField()
    short_url=models.CharField(max_length=20,unique=True)


# class Admin(models.Model):
#     id = models.AutoField(primary_key=True)
#     username=models.CharField(max_length=100,blank=False,unique=True)
#     password=models.CharField(max_length=100,blank=False)
#
# #     class Meta:
#         db_table="admin_table"
#
#     def __str__(self):
#         return self.username
