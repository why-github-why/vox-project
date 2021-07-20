from django.shortcuts import render
from django.http import HttpResponse


def customers(request):
   return HttpResponse('<h1 style="text-align: center;">Customers</h1>')
