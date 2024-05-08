"""
URL configuration for ofs2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from customer import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('customer_dashboard', views.customer_dashboard, name='customer_dashboard'),
    path('about', views.about, name='about'),

    # login 
    path('login', views.login, name='login'),
    path('login_check', views.login_check, name='login_check'),
    path('logout', views.logout, name='logout'),

    #register
    path('register', views.register, name='register'),
    path('register_store', views.register_store, name='register_store'),
    
    #profile
    path('profile', views.profile, name='profile'),
    path('profile_edit/<int:id>', views.profile_edit, name='profile_edit'),
    path('profile_update/<int:id>', views.profile_update, name='profile_update'),

    path('change_password', views.change_password, name='change_password'),
    
    path('cart', views.cart, name='cart'),
    path('cart_add/<int:id>', views.cart_add, name='cart_add'),
    path('item_clear/<int:id>', views.item_clear, name='item_clear'),
    path('item_increment/<int:id>', views.item_increment, name='item_increment'),
    path('item_decrement/<int:id>', views.item_decrement, name='item_decrement'),
    path('cart_clear', views.cart_clear, name='cart_clear'),

    path('check_out', views.check_out, name='check_out'),
    path('orderstore', views.orderstore, name='orderstore'),
    path('customer_feedback', views.customer_feedback, name='customer_feedback'),
    path('feedback_store', views.feedback_store, name='feedback_store'),
    path('inquiry', views.inquiry, name='inquiry'),
    path('inquiry_store', views.inquiry_store, name='inquiry_store'),

    path('category/<int:id>', views.category, name='category'),
    path('subcategory/<int:id>', views.subcategory, name='subcategory'),
    path('detail/<int:id>', views.detail, name='detail'),
    path('detail_add/<int:id>', views.detail_add, name='detail_add'),
    path('payment_process', views.payment_process, name='payment_process'),
    path('success', views.success, name='success'),

    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='customer/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='customer/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='customer/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='customer/password_reset_complete.html'), name='password_reset_complete')
]  