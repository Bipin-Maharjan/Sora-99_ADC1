from django.shortcuts import render,redirect,HttpResponse
from django.http import HttpResponse,Http404,HttpResponseForbidden
from .models import Book,Review,Transaction,UserInfo
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .CustomException import CustomException

# Create your views here.
def login_url(request): #this is for demo remove for final uplaod
  return HttpResponse("<h1>required login to view page</h1> go to adimn <a href='/admin'>admin</a>")

def loadBook(request):
  books = Book.objects.all()
  return render(request,'ReadBook/Book.html',context={'books':books})

def bookDescription(request,bid):
  book = None
  reviews = None
  bought = False
  hadreview = None
  loggedin = True if request.user.is_authenticated else False 
  try:
    if Book.objects.filter(id=bid).exists():
      book = Book.objects.get(id=bid)
      reviews = Review.objects.filter(book_id = bid).order_by('date').all()[:5]
    else:
      #no book found of that id
      raise Http404

    if loggedin:
      #check if user have bought this book 
      bought = True if Transaction.objects.filter(user_id=request.user.id,book_id=bid).exists() else Book.objects.filter(id = bid , book_type = "Free").exists()
      if bought :
        #check if user have review this book
        hadreview = Review.objects.filter(user_id=request.user.id,book_id=bid).all()
        hadreview = '' if len(hadreview) == 0 else hadreview[0]

  except Http404:
    raise Http404('Book not found')
  except Exception as e:
    message.error(request,"Internal Servre Error.")
    print("Error in bookDescription :"+str(e))

  return render(request,'ReadBook/BookDescription.html',context={
    'book':book,
    'reviews':reviews,
    "loggedin":loggedin,
    "bought":bought,
    "hadreview":hadreview
    })

@login_required(login_url='/login/')
def review(request,bid):
  review = None
  user = None
  try:
    if request.method == "POST":
      if Book.objects.filter(id = bid).exists():
        review = request.POST.get('review','').strip()
        user = request.user
        #checking if book has been bought or not
        if (Transaction.objects.filter(user_id=user.id,book_id=bid).exists()) or (Book.objects.filter(id = bid , book_type = "Free").exists()): 
          if review == '' :
            raise CustomException('Review is Null')
          elif Review.objects.filter(user_id = user.id , book_id = bid).exists():
            #update existing Review
            update_row = Review.objects.filter(user_id = user.id , book_id = bid).get()
            update_row.review = review
            update_row.save()
          else:
            #create new Review
            Review.objects.create(book_id = bid , user_id = user.id, review = review)
        else:
          raise CustomException("You must buy this book to Review this book.")
      else:
        # if no book then redirect to description
        return redirect("ReadBook:description", bid = bid)
    else:
      #if request is get
      # show 404 error page
      raise Http404
  except Http404:
    raise Http404("Review Page Not Found")
  except CustomException as ce:
    messages.error(request,str(ce))
  except Exception as e:
    messages.error(request, 'Error while adding review')
    print("Error in review :"+str(e))
  return redirect("ReadBook:description", bid = bid)

@login_required(login_url='/login/')
def rating(request,bid):
  rating = None
  user = None
  try:
    if request.method == "POST":
      if Book.objects.filter(id = bid).exists():
        rating = int(request.POST.get('star',None))
        user = request.user
        #checking if book has been bought or not
        if (Transaction.objects.filter(user_id=user.id,book_id=bid).exists()) or (Book.objects.filter(id = bid , book_type = "Free").exists()): 
          if rating > 5 or rating < 1 :
            raise CustomException('Rating Not valid')
          elif Review.objects.filter(user_id = user.id , book_id = bid).exists():
            #update existing rating
            update_row = Review.objects.filter(user_id = user.id , book_id = bid).get()
            update_row.rating = rating
            update_row.save()
            #calling function that make change in book_rating cell
            calculateRating(bid)
          else:
            #create new one
            Review.objects.create(book_id = bid , user_id = user.id, rating = rating)
            calculateRating(bid)
        else:
          raise CustomException("You must buy this book to Rate this book.")
      else:
        # if no book then redirect to description
        return redirect("ReadBook:description", bid = bid)
    else:
      #if request is get
      #show 404 error page
      raise Http404
  except Http404:
    raise Http404("Rating Page Not Found")
  except CustomException as ce:
    messages.error(request,str(ce))
  except Exception as e:
    messages.error(request, 'Error while adding your rating')
    print("Error in rating :"+str(e))
  return redirect("ReadBook:description", bid = bid)

@login_required(login_url='/login/')
def addBook(request):
  error = None
  name = ''
  price = ''
  btype = ''
  cover = ''
  pdf = ''
  description=''
  category=''
  userid=''
  if request.method == 'POST':
    try:
      name = request.POST['name'].strip()
      btype = request.POST['type'].strip()
      description = request.POST['description'].strip()
      category = request.POST['category'].strip()
      cover = request.FILES.get('image',None)
      pdf = request.FILES['file']
      userid = request.user.id

      if UserInfo.objects.filter(pk = userid,user_type = "Author").exists():
        #checking book type
        if btype != 'Free':
          price = int(request.POST['price'])
        else:
          price = 0

        #checking for errors
        if (name == '' or btype == '' or description == '' or category == ''):
          raise Exception('Empty Field')
        elif pdf.content_type != 'application/pdf':
          raise Exception('File Type Error')
        elif cover == None:
          cover = 'book_images\\no_cover.jpg'
        elif cover.content_type != 'image/jpeg':
          raise Exception('Image Type Error')
        
        Book.objects.create(book_name=name,book_price=price ,book_type=btype,book_cover=cover,book_description=description,book_category=category,book_file=pdf,uploaded_by_id=userid)
      else:
        raise PermissionDenied
    except PermissionDenied:
      error = "You don not have permission to add book. Please sign up as Author."
    except Exception as e:
      error = "Error while processing the data. This might be because your data is incomplete or incorrect."
      print("ERROR : "+str(e))
    else:
      #if no error in try block this will run
      return redirect('ReadBook:premiumbook')
  else:
    if not UserInfo.objects.filter(pk = request.user.id,user_type = "Author").exists():
      raise PermissionDenied('Sign up as Author to view this page')

  return render(request,'ReadBook/AddBook.html',context={'error':error,'bookname':name,'bookprice':price,'description':description,'category':category})

def calculateRating(bid):
  '''
    TO calculate average rating of the book
  '''
  total = Review.objects.filter(book_id = bid).aggregate(Sum('rating'))
  review_no = Review.objects.filter(book_id = bid).all().count()
  update_row = Book.objects.get(id = bid)
  update_row.book_rating = int(total['rating__sum'])/int(review_no)
  update_row.save()