from django.urls import path,include
from . import views

app_name = "DELETE_API"

urlpatterns = [
  path('delete/id=<int:id>/',views.deleteBook,name="deleteBook"),

]