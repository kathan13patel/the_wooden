from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth,messages
from customer.models import *
from myadmin.models import *
from .models import Feedback
from cart.cart import Cart
from django.contrib.auth.decorators import login_required
import razorpay
from django.views.decorators.csrf import csrf_exempt

def customer_dashboard(request):
	category = Category.objects.all()
	feedback = Feedback.objects.all() 
	context = {'category':category,'feedback':feedback}
	return render(request,'customer/customer_dashboard.html',context)

def about(request):
	category = Category.objects.all()
	context = {'category':category}
	return render(request,'customer/about.html',context)

def inquiry(request):
	category = Category.objects.all()
	context = {'category':category}
	return render(request,'customer/contact.html',context)

#category

def category(request,id):
	category = Category.objects.all()
	single_r = Product.objects.filter(category_id=id)
	selected_category = Category.objects.filter(pk=id)

	subcategory = Sub_category.objects.all()
	sub = Sub_category.objects.filter(category_id=id) 

	context = {'result' : single_r,'category':category,'selected_category': selected_category,'sub':sub}
	return render(request,'customer/category.html',context)

#subcategory

def subcategory(request,id):
	category = Category.objects.all()
	subcategory = Sub_category.objects.all()
	single_r = Product.objects.filter(subcategory_id=id)
	selected_sub_category = Sub_category.objects.filter(pk=id)


	context = {'result': single_r,'selected_sub_category':selected_sub_category,'category':category,'subcategory':subcategory}
	return render(request,'customer/subcategory.html',context)

#single product page

def detail(request,id):
	category = Category.objects.all()
	single_r = Product.objects.filter(category_id=id)
	product = Product.objects.get(pk=id)
	context = {'category':category,'product':product}
	return render(request,'customer/detail.html',context)

def detail_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/customer/check_out")

#login

def login(request):
	category = Category.objects.all()
	context = {'category':category}
	return render(request,'customer/customer_login.html',context)

def login_check(request):
	myuname    = request.POST['username'] 
	mypassword = request.POST['password']

	result = auth.authenticate(username=myuname,password=mypassword)
	if result is None:
		messages.success(request,"!! invalid username or password")
		return redirect('/customer/login') 

	elif result.is_superuser:
		messages.success(request, "!! invalid")
		return redirect('/customer/login')

	else:
		auth.login(request,result)
		return redirect('/customer/customer_dashboard')

def logout(request):
	auth.logout(request)
	return redirect('/customer/login')

#register

def register(request):
	category = Category.objects.all() 
	context = {'category':category}
	return render(request,'customer/registration.html',context)


def register_store(request):
	myfname 	= request.POST['f_name']
	mylname 	= request.POST['l_name']
	myuname     = request.POST['username']
	mypassword  = request.POST['password']
	mycpassword = request.POST['cpassword']
	myemail 	= request.POST['email']

	mycontact 	= request.POST['contact']
	myaddress 	= request.POST['address']

	if mypassword == mycpassword:
		if User.objects.filter(username=myuname).exists():
			messages.success(request,"username already taken")
			return redirect('/customer/register')

		else:	
			result 	= User.objects.create_user(first_name=myfname,last_name=mylname,username=myuname,password=mypassword,email=myemail)
			Profile.objects.create(contact=mycontact,address=myaddress,user_id=result.id)
			return redirect('/customer/login')

	elif login_check() >= 0:
	 	return redirect('/customer/customer_dashboard')

	else:
		messages.success(request,"password mismatch")
		return redirect('/customer/register')

#profile

@login_required(login_url="/customer/login")
def profile(request):
	category = Category.objects.all()
	try:
		id = request.user.id
		profile = Profile.objects.get(user_id = id)
		context = {'profile':profile,'category':category}
		return render(request,'customer/profile.html',context)

	except Profile.DoesNotExist:
		messages.success(request,"Please login again")
		return redirect('/customer/login')

def profile_edit(request,id):
	id = request.user.id
	profile = Profile.objects.get(user_id = id)
	context = {'result' : profile}
	return render(request,'customer/profile_edit.html',context)

def profile_update(request,id):
	myfname 	= request.POST['f_name']
	mylname 	= request.POST['l_name']
	myuname     = request.POST['username']
	myemail 	= request.POST['email']
	mycontact 	= request.POST['contact']
	myaddress 	= request.POST['address']

	data = {'first_name' : myfname, 'last_name' : mylname, 'username' : myuname, 'email' : myemail}
	data1 = {'contact' : mycontact, 'address' : myaddress}

	id = request.user.id
	profile = Profile.objects.get(user_id=id)
	User.objects.update_or_create(pk=id,defaults=data)
	Profile.objects.update_or_create(user_id=id,defaults=data1)
	return redirect('/customer/profile')

@login_required(login_url="/customer/login")
def change_password(request):
    category = Category.objects.all()
    if request.method == "POST":
        user = request.user 
        old_password = request.POST['password']
        new_password = request.POST['npassword']
        con_password = request.POST['cpassword']

        # Check if the old password matches the current password
        if old_password == False:
            messages.error(request, 'Old password is incorrect.')
            return redirect("/customer/change_password")

        # Check if the new password and confirmation match
        elif new_password != con_password:
        	messages.error(request, 'New password and confirm password do not match.')
        	return redirect("/customer/change_password")
        
        else:	
        	user.set_password(new_password)
        	user.save()

        messages.success(request, 'Password changed successfully.')
        return redirect("/customer/login")

    context = {'category':category}

    return render(request, 'customer/change_password.html',context)

@login_required(login_url="/customer/login")
def cart(request):
	category = Category.objects.all()
	context = {'category':category} 
	return render(request,'customer/cart.html',context)

@login_required(login_url="/customer/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/customer/cart")

@login_required(login_url="/customer/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("/customer/cart")

@login_required(login_url="/customer/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("/customer/cart")

@login_required(login_url="/customer/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id,)
    cart.decrement(product=product)
    return redirect("/customer/cart")

@login_required(login_url="/customer/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/customer/cart") 

def orderstore(request):
	uid         = request.user.id
	myname 		= request.POST['name']
	myemail 	= request.POST['email']	
	myaddress 	= request.POST['address']
	mycontact 	= request.POST['contact']
	mydetails 	= request.POST['details']
	mytotal 	= request.POST['total']
	mytype      = request.POST['payment']

	cart = Cart(request)
	orders = Order.objects.create(user_id=uid,name=myname,email=myemail,address=myaddress,
		mobile=mycontact,details=mydetails,total=mytotal,pay_type=mytype)
	if mytype == 'online':
		cart.clear()
		return redirect('/customer/payment_process')
	else:
		cart.clear()
		return redirect('/customer/success')
	
@login_required(login_url="/customer/login")
def check_out(request):
	category = Category.objects.all()
	try:
		id = request.user.id
		profile = Profile.objects.get(user_id = id)
		context = {'profile': profile,'category':category}
		return render(request,'customer/check_out.html',context)

	except Profile.DoesNotExist:
		messages.success(request,"Please login again")
		return redirect('/customer/login')

def customer_feedback(request):
	if request.user.is_authenticated:
		category = Category.objects.all()
		context = {'category':category}
		return render(request,'customer/feedback.html',context)

	else:
		return redirect('/customer/login')

def feedback_store(request):
	myrating  = request.POST['rating']
	mycomment = request.POST['comment']
	myuser_id = request.user.id

	Feedback.objects.create(rating=myrating,comment=mycomment,user_id=myuser_id)
	return redirect('/customer/customer_feedback')

def inquiry_store(request):
	myname 	  = request.POST['name']
	myemail   = request.POST['email']
	mymobile  = request.POST['mobile']
	mysubject = request.POST['subject']
	mymessage = request.POST['message']

	Inquiry.objects.create(name=myname,email=myemail,mobile=mymobile,subject=mysubject,message=mymessage)
	messages.success(request,"successfully sent")
	return redirect('/customer/inquiry')

def payment_process(request):
    key_id = 'rzp_test_PvM4GxK9MYlCUc'
    key_secret = 'WzsOTRAU4l3oAA1CS7jlVS5E'

    obj= Order.objects.filter(user_id=request.user.id).order_by('-id')[0]
    amount = float(obj.total) * 100

    client = razorpay.Client(auth=(key_id, key_secret))
 
    data = {
        'amount': amount,
        'currency': 'INR',
        "receipt":"OIBP",
        "notes":{
            'name' : 'AK',
            'payment_for':'OIBP Test'
        }
    }
    id = request.user.id
    category = Category.objects.all()
    result = User.objects.get(pk=id)
    payment = client.order.create(data=data)
    context = {'payment' : payment,'result':result,'order':obj,'category':category}
    return render(request, 'customer/payment_process.html',context)

@csrf_exempt
def success(request):
	category = Category.objects.all()
	context = {'category':category}
	return render(request,'customer/payment_success.html',context)
