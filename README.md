# Sora-99_ADC1
 Coursework on E-Library
 
## Group Name: Sora-99
### Members Name : 
- Shradha Limbu
- Manil Maharjan
- Bipin Maharjan
 
 
### Requirement:
 - Install pillow: ``` $ pip install pillow ```
 
### Setting up this project:
- ```python manage.py makemigration```
- ```python manage.py migrate```
- ```python manage.py runserver```

### Built on Django Version: 3.0.1
> Enjoy the code !!!

#  API Documentation


## GET API
- To get first 10 books
  syntax : /api/book/
  usage : 127.0.0.1:8000/api/book/

- To get Book By ID
  syntax : /api/book/id=<int:id>/
  usage : 127.0.0.1:8000/api/book/id=1/

- To get book by page number and size
  syntax : /api/book/page=<int:page>/size=<int:size>/
  usage : 127.0.0.1:8000/api/book/page=1/size=5/

- To get first 10 reviews
  syntax : /api/review/book=<int:bookid>/
  usage : 127.0.0.1:8000/api/review/book=1/

- To get reviews by page number and size
  syntax : /api/review/book=<int:bookid>/page=<int:page>/size=<int:size>/
  usage : 127.0.0.1:8000/api/review/book=1/page=2/size=5/
  
- To Delete Book by id
  syntax : /api/delete/book=<int:bookid>
  usage : 127.0.0.1:8000/api/delete/book=1

- To search book through keyword.
> The default page size of search API is limit to 5. Increase page number to view more
  syntax : /book/search?q="keyword"
  synatx : /book/search?q="keyword"&page="Number"
  usage : 127.0.0.1:8000/book/searchq?q="python"&page="2"
