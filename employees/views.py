from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from .models import Employee

def register(request):
   if request.method == 'POST':
      username = request.POST['username']
      email = request.POST['email']
      phone = request.POST['phone']
      password = request.POST['password']
      confirm_password = request.POST['confirm_password']

      # check if passwords match
      if password == confirm_password:

         # check if username already exists in db
         if User.objects.filter(username=username).exists():
            messages.error(request, 'Username is already taken.')
            return redirect('register')
         else:
            # check if email already exists in db
            if User.objects.filter(email=email).exists():
               messages.error(request, 'Email is already being used.')
               return redirect('register')
            else:
               # create user
               user = User.objects.create_user(
                  username = username,
                  email = email,
                  password = password,
               )
               user.save()

               # create employee
               employee = Employee(
                  username = username,
                  email = email,
                  phone = phone,
               )
               employee.save()

               messages.success(request, 'You are now registered.')
               return redirect('login')

      else:
         messages.error(request, 'Passwords doesn\'t match.')
         return redirect('register')

   else:
      return render(request, 'employees/register.html')


def login(request):
   if request.method == 'POST':
      # acquire login credentials
      username = request.POST['username']
      password = request.POST['password']

      # authenticate employee
      employee = auth.authenticate(username=username, password=password)

      # check if employee is registered
      if employee is not None:
         auth.login(request, employee)
         messages.success(request, 'You logged in successfully.')
         return redirect('customers')
      else:
         messages.error(request, 'Invalid credentials.')
         return redirect('login')

   else:
      return render(request, 'employees/login.html')


def logout(request):
   if request.method == 'POST':
      # logout employee
      auth.logout(request)
      messages.success(request, 'You are now logged out.')
      return redirect('login')


# def register(request):
#    if request.method == 'POST':
#       username = request.POST['username']
#       email = request.POST['email']
#       phone = request.POST['phone']
#       password = request.POST['password']
#       confirm_password = request.POST['confirm_password']

#       # check if passwords match
#       if password == confirm_password:

#          # check if username already exists in db
#          if Employee.objects.filter(username=username).exists():
#             messages.error(request, 'Username is already taken.')
#             return redirect('register')
#          else:
#             # check if email already exists in db
#             if Employee.objects.filter(email=email).exists():
#                messages.error(request, 'Email is already being used.')
#                return redirect('register')
#             else:
#                # create user
#                employee = Employee(
#                   username = username,
#                   email = email,
#                   phone = phone,
#                   password = password,
#                )
#                employee.save()
#                messages.success(request, 'You are now registered.')
#                return redirect('login')

#       else:
#          messages.error(request, 'Passwords doesn\'t match.')
#          return redirect('register')

#    else:
#       return render(request, 'employees/register.html')