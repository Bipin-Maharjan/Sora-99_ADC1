from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path('', views.getBook, name= 'getBook'),
	path('getBook/', views.authorSplit, name ='authorSplit'), 
    path('admin/', admin.site.urls),
]