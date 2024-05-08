from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profile(models.Model):
	contact = models.BigIntegerField()
	address = models.TextField()
	user    = models.OneToOneField(User, on_delete=models.CASCADE)

	class Meta:
		db_table = 'profile'

class Feedback(models.Model):
	rating = models.CharField(max_length=10)
	comment = models.TextField()
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	date = models.DateField(default=date.today())

	class Meta:
		db_table = 'feedback'

class Inquiry(models.Model):
	name = models.CharField(max_length=30)
	email = models.CharField(max_length=50)
	mobile = models.BigIntegerField()
	subject = models.CharField(max_length=30)
	message = models.TextField()
	date = models.DateField(default=date.today())

	class Meta:
		db_table = 'inquiry'

class Order(models.Model):
	user    	= models.ForeignKey(User,on_delete=models.CASCADE,default="")
	name 		= models.CharField(max_length=30)
	email 		= models.CharField(max_length=50)
	mobile 		= models.BigIntegerField()
	address 	= models.TextField()
	details 	= models.TextField()
	total   	= models.CharField(max_length=10)
	date 		= models.DateField(default=date.today())
	pay_type    = models.CharField(max_length=30,default="")

	class Meta:
		db_table = 'order' 
		ordering = ['date']