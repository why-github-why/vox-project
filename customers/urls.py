from django.urls import path
from . import views

urlpatterns = [
   path('', views.customers, name='customers'),
   path('create', views.create, name='create'),
   path('search', views.search, name='search'),
   path('modify/<int:customer_id>', views.modify, name='modify'),
   path('display', views.display, name='display'),
]
