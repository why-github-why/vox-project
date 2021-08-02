from django.db import models
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib import messages, auth
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import Customer


def customers(request):
   return render(request, 'customers/customers.html')


def create(request):
   if request.method == 'POST':
      customer_id = request.POST['customer_id']
      company_name = request.POST['company_name']
      customer_email = request.POST['customer_email']
      customer_phone = request.POST['customer_phone']
      user_id = request.POST['user_id']

      customer = Customer(
         customer_id = customer_id,
         company_name = company_name,
         customer_email = customer_email,
         customer_phone = customer_phone,
         user_id=user_id,
      )
      customer.save()

      messages.success(request, 'Customer created.')
      return redirect('customers')

   else:
      # check if any customer ID starts with user ID
      any_customers = Customer.objects.filter(customer_id__startswith=request.user.id)

      if not any_customers:
         # if not, new ID = user ID with two trailing zeros
         new_id = f"{request.user.id}00"
         customer_id = int(new_id)
      else:
         # if so, increment customer ID by 1
         latest_customer = any_customers.order_by('customer_id').last()
         customer_id = latest_customer.customer_id + 1

      context = {
         'customer_id': customer_id,
      }

      return render(request, 'customers/create.html', context)


def modify(request):
   if request.method == 'GET':
      customer_id = request.GET['customer_id']
      search_user = Customer.objects.filter(user=request.user)
      search_query = search_user.filter(customer_id__iexact=customer_id)
         
      context = {
         'results': search_query,
      }

      return render(request, 'customers/modify.html', context)

   else:
      # modify existing object via current customer ID
      # modified object as dict
      modified_object = {
         "customer_id": request.POST['customer_id'],
         "company_name": request.POST['company_name'],
         "customer_email": request.POST['customer_email'],
         "customer_phone": request.POST['customer_phone'],
         "user_id": request.POST['user_id'],
      }

      # objects.get - get current dict
      customer = Customer.objects.get(customer_id=modified_object['customer_id'])

      # setattr - sets the value of an objects attribute
      # iterate through current dict and update each entry
      for key, value in modified_object.items():
         setattr(customer, key, value)

      # save modified object (dict)
      customer.save()

      messages.success(request, 'Customer modified.')
      return redirect('customers')


def delete(request):
   if request.method == "POST":
      customer = Customer.objects.filter(customer_id=request.POST['customer_id'], user_id=request.POST['user_id'])
      customer.delete()

      messages.success(request, 'Customer deleted.')
      return redirect('customers')


def display(request):
   display_object = Customer.objects.filter(user=request.user)
   print(display_object)
   paginator = Paginator(display_object, 1)
   page = request.GET.get('page')
   display_all = paginator.get_page(page)

      
   context = {
      'display_customers': display_all,
      'total_entries': paginator.count,
   }

   return render(request, 'customers/display.html', context)
