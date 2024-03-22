from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Employee(models.Model):
    EmpId = models.CharField(max_length=3)
    EmpName = models.CharField(max_length=200)
    EmpGender = models.CharField(max_length=10)
    EmpEmail = models.EmailField()
    EmpDesignation = models.CharField(max_length=150)
    class Meta:
        db_table="Employee"

from . import views
from django.urls import path

urlpatterns = [
    path('', views.insert_emp, name='insert-emp'),
    path('show/', views.show_emp, name='show-emp'),
    path('edit/<int:pk>', views.edit_emp, name='edit-emp'),
    path('remove/<int:pk>', views.remove_emp, name='remove-emp'),
]

