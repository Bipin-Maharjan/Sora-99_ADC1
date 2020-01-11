from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path('', views.getBook, name= 'getBook'),
	path('/home', views.home, name ='homepage'), 
    path('admin/', admin.site.urls),
]
#{% url 'home' %}