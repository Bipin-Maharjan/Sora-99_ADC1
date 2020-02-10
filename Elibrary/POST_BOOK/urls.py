from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path('add-book/', views.postBook, name='addbook'),
]