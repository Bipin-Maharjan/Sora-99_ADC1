from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserInfo(models.Model):
  #linking to user model through one to one relation
  users = models.OneToOneField(User, on_delete=models.CASCADE)

  #additional
  user_type = models.CharField(max_length=6)
  user_amount = models.IntegerField(default=0)

  def __str__(self):
    return self.users.username

class Book(models.Model):
  book_name = models.CharField(max_length=50)
  uploaded_by = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  book_price = models.IntegerField(default=0)
  book_type = models.CharField(max_length=10)
  book_discount = models.IntegerField(default=0)
  #book_image = models.ImageField(upload_to='book_images/')
  book_description = models.TextField()
  book_category = models.CharField(max_length=30)
  book_file = models.FileField(upload_to='book/')
  def __str__(self):
    return str(self.book_name)

class PaymentDetail(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  book = models.ForeignKey(Book,on_delete=models.CASCADE)
  user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  price = models.IntegerField(null=False)
  discount = models.IntegerField(default=0)

  def __str__(self):
    return str(self.book) + " ==> "+ str(self.user)

class PendingPayment(models.Model):
  date = models.DateTimeField(auto_now_add=True)
  book = models.ForeignKey(Book,on_delete=models.CASCADE)
  user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
  price = models.IntegerField(null=False)
  discount = models.IntegerField(default=0)

  def __str__(self):
    return str(self.book) + " ==> "+ str(self.user)

class Review(models.Model):
  book = models.ForeignKey(Book, on_delete=models.CASCADE)
  rating = models.SmallIntegerField()
  review = models.TextField()
  date = models.DateTimeField(auto_now_add=True)
  user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)

  def __str__(self):
    return str(self.book) + " - " + str(self.user) + " - " + str(self.rating)