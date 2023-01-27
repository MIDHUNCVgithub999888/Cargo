from django.db import models
from django.core.validators import RegexValidator
from  datetime import datetime,date 

# Create your models here.

class EmployeeRegisterTB(models.Model):
	Name=models.CharField(max_length=100,default='')
	Dateofjoin=models.DateField(auto_now_add=False, auto_now=False,null=True)
	Age=models.IntegerField(null=True)
	Gender=models.CharField(max_length=100,default='')
	Address=models.CharField(max_length=100,default='')
	City=models.CharField(max_length=100,default='')
	State=models.CharField(max_length=100,default='')
	Country=models.CharField(max_length=100,default='')
	Photo=models.ImageField(upload_to="media/",default='')
	EmailID=models.EmailField(default='')
	Phonenumber=models.CharField(max_length=100,default='')
	Loginname=models.CharField(max_length=100,default='')
	Password=models.CharField(max_length=100,default='')
	ConfirmPassword=models.CharField(max_length=100,default='')
	Status=models.CharField(max_length=100,default='')

def __str__(self):
	return self.Name


class AdminBranchesTB(models.Model):
	BranchName=models.CharField(max_length=100,default='')
	BranchContactnumber=models.CharField(max_length=100,default='')
	BranchEmail=models.EmailField()
	BranchAddress=models.CharField(max_length=100,default='')
	BranchCity=models.CharField(max_length=100,default='')
	BranchState=models.CharField(max_length=100,default='')
	BranchPincode=models.CharField(max_length=100,default='')
	BranchCountry=models.CharField(max_length=100,default='')

def __str__(self):
	return self.BranchName






	
