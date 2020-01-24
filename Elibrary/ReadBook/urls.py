from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "ReadBook"

urlpatterns = [
    path('', views.loadBook, name='premiumbook'),
    path('description/<int:bid>/', views.bookDescription, name='description'),
    path('addbook/', views.addBook, name='addbook'),
    path('review/<int:bid>/', views.review, name="review"),
    path('rating/<int:bid>/', views.rating, name='rating')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
