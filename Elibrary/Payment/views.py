from django.shortcuts import render 
from ReadBook.models import UserInfo, Book, PaymentDetail

def getBook(request):
	book = Book.objects.get(id=1)
	dis = (int (book.book_discount) * int(book.book_price))/100
	total= book.book_price - dis
	return render(request,'transaction.html', context={'book':book, 'total': total})


def authorSplit(request):
	total= 100
	user = UserInfo.objects.filter(user_type ='Author', users_id =1).get()
	amou = (int(total) * 60)/100
	user.user_amount = int(user.user_amount) + amou
	user.save()
	return render(request,'home.html', context = {'amount':user.user_amount})
	
'''def userAmo(request):
	total = 100
	useram=UserInfo.objects.filter(user_type = 'Reader', users_id =2).get()
    pay = (int (user.user_amount)) - total
    payment.user_amount = UserInfo.objects.filter(users_id = 2). update(user_amount=pay)
 	payment.save()
 	return render(request, 'home.html', context = {'useramount':payment})

def userSplit(request):
	total = 100
	user = UserInfo.objects.filter(user_type ='Admin').get()
	amou = (int(total)*40)/100
	admin.admin_amount = int (admin.admin_amount)+amou
	admin.save()
	return render(request, 'admin.html', context={'admin': admin.admin_amount})'''