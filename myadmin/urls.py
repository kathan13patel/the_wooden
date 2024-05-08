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
from myadmin import views

urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('admin_login', views.admin_login, name='admin_login'),
    path('admin_login_check', views.admin_login_check, name='admin_login_check'),
    path('mylogout', views.mylogout, name='mylogout'),

    #category

    path('category', views.category, name='category'),
    path('category_store', views.category_store, name='category_store'),
    path('category_read', views.category_read, name='category_read'),
    path('category_edit/<int:id>', views.category_edit, name='category_edit'),
    path('category_delete/<int:id>', views.category_delete, name='category_delete'),
    path('category_update/<int:id>', views.category_update, name='category_update'),
    
    #sub category

    path('subcategory', views.subcategory, name='subcategory'),
    path('sub_category_store', views.sub_category_store, name='sub_category_store'),
    path('sub_category_read', views.sub_category_read, name='sub_category_read'),
    path('sub_category_edit/<int:id>', views.sub_category_edit, name='sub_category_edit'),
    path('sub_category_delete/<int:id>', views.sub_category_delete, name='sub_category_delete'),
    path('sub_category_update/<int:id>', views.sub_category_update, name='sub_category_update'),

    # product
    
    path('product', views.product, name='product'),
    path('product_store', views.product_store, name='product_store'),
    path('product_read', views.product_read, name='product_read'),
    path('product_edit/<int:id>', views.product_edit, name='product_edit'),
    path('product_delete/<int:id>', views.product_delete, name='product_delete'),
    path('product_update/<int:id>', views.product_update, name='product_update'),

    # customer
    path('customer_read', views.customer_read, name='customer_read'),
    path('inquiry_read', views.inquiry_read, name='inquiry_read'),
    path('inquiry_delete/<int:id>', views.inquiry_delete, name='inquiry_delete'),

    path('order_read', views.order_read, name='order_read'),
    # path('payment_read', views.payment_read, name='payment_read'),
    path('order_delete/<int:id>', views.order_delete, name='order_delete'),

    path('feedback', views.feedback, name='feedback'),
    path('feedback_delete/<int:id>', views.feedback_delete, name='feedback_delete'),
    
    path('delivery_boy', views.delivery_boy, name='delivery_boy'),
    path('db_read', views.db_read, name='db_read'),
    path('db_store', views.db_store, name='db_store'),
    path('db_edit/<int:id>', views.db_edit, name='db_edit'),
    path('db_delete/<int:id>', views.db_delete, name='db_delete'),
    path('db_update/<int:id>', views.db_update, name='db_update')
]
