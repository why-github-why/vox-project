from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.http import HttpResponse
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
      print(any_customers)

      if not any_customers:
         # if not, new ID = user ID with two trailing zeros
         new_id = f"{request.user.id}00"
         customer_id = int(new_id)
         print("New ID created.")
      else:
         # if so, increment customer ID by 1
         latest_customer = any_customers.order_by('customer_id').last()
         print(latest_customer)
         customer_id = latest_customer.customer_id + 1
         print(customer_id)
         print("Latest customer.")


      context = {
         'customer_id': customer_id,
      }
      return render(request, 'customers/create.html', context)


def modify(request):
   return HttpResponse('<h1 style="text-align:center;">Modify</h1>')


def display(request):
   return HttpResponse('<h1 style="text-align:center;">Display</h1>')
