from django.shortcuts import render,redirect
from django.contrib import auth,messages
from django.contrib.auth import authenticate, login
from myadmin.models import *
from customer.models import *
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from cart.cart import Cart
from django.contrib.auth.decorators import login_required

@login_required(login_url="/myadmin/admin_login")
def dashboard(request):
	superuser = User.objects.filter(is_superuser=True).first() 
	total_users = User.objects.count()

	total_sum = 0
	for item in Order.objects.all():
		total_sum += float(item.total)

	total_user = Inquiry.objects.count()
	total_product = Product.objects.count()
	context = {'super':superuser,'total':total_users,'order':total_sum,'inquiry':total_user,'product':total_product}
	return render(request,'myadmin/dashboard.html',context)

#login

def admin_login(request):
	context = {}
	return render(request,'myadmin/admin_login.html',context)

def admin_login_check(request):
    username = request.POST['username']
    password = request.POST['password']

    result = auth.authenticate(username=username,password=password)

    if result is None:
    	messages.success(request,"invalid username or password")
    	return redirect('/myadmin/admin_login')

    elif result.is_superuser == False:
    	messages.success(request,"Only admin can login")
    	return redirect('/myadmin/admin_login')

    else:
    	auth.login(request,result)
    	return redirect('/myadmin/dashboard')

#logout

def mylogout(request):
	auth.logout(request)
	return redirect('/myadmin/admin_login')	

#category

def category(request):
	context = {}
	return render(request,'myadmin/add_category.html',context)

def category_store(request):
	mycategory = request.POST['category']

	Category.objects.create(category_name = mycategory)
	return redirect('/myadmin/category')

def category_read(request):
	category_result = Category.objects.all()
	context 	    = {'result' : category_result}
	return render(request,'myadmin/category_read.html',context) 

def category_edit(request,id):
	result  = Category.objects.get(pk=id)
	context = {'result' : result}
	return render(request,'myadmin/category_edit.html',context)

def category_delete(request,id):
	result = Category.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/category_read')  

def category_update(request,id):
	mycategory = request.POST['category']

	data = { 'category_name' : mycategory }

	Category.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/category_read')

#subcategory

def view_sub_category(request):
	context = {}
	return render(request,'myadmin/view_sub_category.html',context)

def subcategory(request):
	category = Category.objects.all()
	context  = {'category':category}
	return render(request,'myadmin/add_sub_category.html',context)

def sub_category_store(request):
	mysubcategory = request.POST['subcategory']
	mycategory    = request.POST['category']

	Sub_category.objects.create(sub_cat_name=mysubcategory,category_id=mycategory)
	return redirect('/myadmin/subcategory')

def sub_category_read(request):
	sub_category_result = Sub_category.objects.all()
	context 			= {'result' : sub_category_result}
	return render(request,'myadmin/sub_category_read.html',context)

def sub_category_edit(request,id):
	result   = Sub_category.objects.get(pk=id)
	category = Category.objects.all()
	context  = {'result' : result,'category':category}
	return render(request,'myadmin/sub_category_edit.html',context)

def sub_category_delete(request,id):
	result = Sub_category.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/sub_category_read')

def sub_category_update(request,id):
	mysubcategory = request.POST['subcategory']
	mycategory 	  = request.POST['category']

	data = { 'sub_cat_name' : mysubcategory,'category_id' : mycategory}

	Sub_category.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/sub_category_read')

# product

def product(request):
	category = Category.objects.all()
	subcategory = Sub_category.objects.all()
	context = {'category':category,'subcategory':subcategory}
	return render(request,'myadmin/add_product.html',context)

def product_store(request):
	myproduct 	  = request.POST['product_name']
	myprice 	  = request.POST['price']
	mydescription = request.POST['description']
	myimage 	  = request.FILES['image']
	mycategory 	  = request.POST['category']
	mysubcategory = request.POST['subcategory']

	mylocation = os.path.join(settings.MEDIA_ROOT,'myadmin')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myimage.name,myimage)

	Product.objects.create(name=myproduct,price=myprice,description=mydescription,image=myimage.name, category_id=mycategory,
		subcategory_id=mysubcategory)
	return redirect('/myadmin/product')

def product_read(request):
	product_result = Product.objects.all()
	context 	   = {'result' : product_result}
	return render(request,'myadmin/product_read.html',context)

def product_edit(request,id):
	result   = Product.objects.get(pk=id)
	category = Category.objects.all()
	subcategory = Sub_category.objects.all()
	context  = {'result' : result,'category':category,'subcategory':subcategory}
	return render(request,'myadmin/product_edit.html',context)

def product_delete(request,id):
	result = Product.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/product_read')

def product_update(request,id):
	myproduct 	  = request.POST['product_name']
	myprice 	  = request.POST['price']
	mydescription = request.POST['description']
	myimage 	  = request.FILES['image']
	mycategory 	  = request.POST['category']
	mysubcategory = request.POST['subcategory']

	mylocation = os.path.join(settings.MEDIA_ROOT,'myadmin')
	obj = FileSystemStorage(location=mylocation)
	obj.save(myimage.name,myimage)

	data = {'name':myproduct,'price':myprice,'description':mydescription,'image':myimage.name,
	'category_id':mycategory,'subcategory_id':mysubcategory}
	Product.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/product_read')

#customer

def customer_read(request):
	users = User.objects.select_related('profile') 
	context = {'result': users}  
	return render(request, 'myadmin/customer_read.html', context)

#inquiry

def inquiry_read(request):
	inquiry_result = Inquiry.objects.all()
	context	= {'result': inquiry_result}
	return render(request,'myadmin/inquiry_read.html',context)

def inquiry_delete(request,id):
	result = Inquiry.objects.get(pk=id)
	result.delete()
	return redirect('/myadmin/inquiry_read')

# order

def order_details(request):
	context = {}
	return render(request,'myadmin/order_details.html',context)

def order_read(request):
	order_result = Order.objects.all()
	context = {'result':order_result}
	return render(request,'myadmin/order_details.html',context)

def order_delete(request,id):
	order_result = Order.objects.get(pk=id)
	order_result.delete()
	return redirect('/myadmin/order_read')

# feedback

def feedback(request):
	feedback = Feedback.objects.all().select_related('user') 
	context = {'feedback':feedback}
	return render(request,'myadmin/feedback.html',context)

def feedback_delete(request,id):
	feedback = Feedback.objects.get(pk=id) 
	feedback.delete()
	return redirect(request,'/myadmin/feedback')

def delivery_boy(request):
	context = {}
	return render(request,'myadmin/add_db.html',context)

def db_store(request):
	myfname 	= request.POST['fname']
	mylname     = request.POST['lname']
	myemail 	= request.POST['email']
	mycontact 	= request.POST['contact']
	myaddress 	= request.POST['address']

	Deliveryboy.objects.create(db_fname=myfname,db_lname=mylname,email=myemail,mobile=mycontact,address=myaddress)
	return redirect('/myadmin/delivery_boy')

def db_read(request):
	db_result = Deliveryboy.objects.all()
	context = {"result":db_result}
	return render(request,'myadmin/db_read.html',context)

def db_edit(request,id):
	result   = Deliveryboy.objects.get(pk=id)
	context  = {'result' : result,}
	return render(request,'myadmin/db_edit.html',context)

def db_delete(request,id):
	db_result = Deliveryboy.objects.get(pk=id)
	db_result.delete()
	return render(request,'myadmin/db_read.html')

def db_update(request,id):
	myfname 	= request.POST['fname']
	mylname     = request.POST['lname']
	myemail 	= request.POST['email']
	mycontact 	= request.POST['contact']
	myaddress 	= request.POST['address']

	data = {'db_fname':myfname,'db_lname':mylname,'email':myemail,'mobile':mycontact,
	'address':myaddress}
	Deliveryboy.objects.update_or_create(pk=id,defaults=data)
	return redirect('/myadmin/db_read')