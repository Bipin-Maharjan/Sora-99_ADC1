from django.contrib import admin
from . models import *

# Register your models here.

#uncomment this after creating database
admin.site.register(UserInfo)
admin.site.register(Book)
admin.site.register(PaymentDetail)
admin.site.register(PendingPayment)
admin.site.register(Review)