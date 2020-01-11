from django.shortcuts import render 
from ReadBook.models import UserInfo, Book, PaymentDetail

def getBook(request):
	book = Book.objects.get(id=1)
	dis = (int (book.book_discount) * int(book.book_price))/100
	total= book.book_price - dis
	return render(request,'transaction.html', context={'book':book, 'total': total})
	
def home(request):
	return render(request, 'home.html')
