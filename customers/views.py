from django.shortcuts import render
from django.http import HttpResponse


def customers(request):
   return render(request, 'customers/customers.html')


def create(request):
   return HttpResponse('<h1 style="text-align:center;">Create</h1>')


def modify(request):
   return HttpResponse('<h1 style="text-align:center;">Modify</h1>')


def display(request):
   return HttpResponse('<h1 style="text-align:center;">Display</h1>')
