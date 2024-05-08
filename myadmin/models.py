from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import date
from customer.models import *
# from cart.cart import Cart
# from .models import Cart  # Import your Cart model

# myadmin.site.register(Cart)

# class Admin(models.Model):
# 	admin_name 	   	   = models.CharField(max_length=50)
# 	username           = models.CharField(max_length=20)
# 	email		       = models.CharField(max_length=50)
# 	password           = models.CharField(max_length=20)
# 	dob			       = models.DateField()
# 	gender			   = models.CharField(max_length=10)
# 	contact		       = models.BigIntegerField()
# 	address			   = models.CharField(max_length=255)


# 	class Meta:
# 		db_table='admin'

# 	def _str_(self):
# 		return self.admin_name

class Category(models.Model):
	category_name = models.CharField(max_length=255)

	def __str__(self):
		return self.category_name

	class Meta:
		db_table = 'category'

class Sub_category(models.Model):
	sub_cat_name = models.CharField(max_length=255,blank=True, null=True,default='')
	category 	 = models.ForeignKey(Category,on_delete=models.CASCADE,default='')

	def __str__(self):
		return self.sub_cat_name

	class Meta:
		db_table = 'sub_category'

class Product(models.Model):
	name 		 = models.CharField(max_length=255)
	price 		 = models.DecimalField(max_digits=7,decimal_places=2)
	description  = models.TextField()
	image 		 = models.CharField(max_length=255)
	category 	 = models.ForeignKey(Category,on_delete=models.CASCADE)
	subcategory  = models.ForeignKey(Sub_category,on_delete=models.CASCADE,default='')

	class Meta:
		db_table = 'product' 

class Deliveryboy(models.Model):
	db_fname  = models.CharField(max_length=30)
	db_lname  = models.CharField(max_length=30)
	mobile 	  = models.BigIntegerField()
	email 	  = models.CharField(max_length=50)
	address   = models.TextField()

	class Meta:
		db_table = 'deliveryboy'

# class Order(models.Model):	
# 	product = models.ForeignKey(Product,on_delete=models.CASCADE)
# 	user = models.ForeignKey(User,on_delete=models.CASCADE)
# 	date = models.DateField(default=date.today())
# 	profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
# 	# cart = models.ForeignKey(Cart,on_delete=models.CASCADE)

# 	class meta:
# 		db_table = 'order' 

# class Cart(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.CharField(max_length=255)
#     quantity = models.IntegerField(default=1)
#     date = models.DateField(default=date.today())

#     def __str__(self):
#         return f"{self.quantity} x {self.product}"

#     def get_absolute_url(self):
#         return reverse("cart:cart")

#     class Meta:       
#    		db_table = 'cart'


# class Customer(models.Model):
# 	mobile  = models.BigIntegerField()
# 	address = models.TextField()
# 	user    = models.OneToOneField(User,on_delete=models.CASCADE)

# 	class Meta:
# 		db_table = 'customer'