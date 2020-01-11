from django.contrib import admin
from . models import *

admin.site.register(UserInfo)
admin.site.register(Book)
admin.site.register(PaymentDetail)
admin.site.register(PendingPayment)
admin.site.register(Review)