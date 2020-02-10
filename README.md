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
- ```python manage.py makemigrations```
- ```python manage.py migrate```
- ```python manage.py runserver```

### Built on Django Version: 3.0.1
> Enjoy the code !!!

#
# API Documentation

#### GET API
- **To get first 10 books**
  - Syntax : ```/api/book/```
  - Usage : ```127.0.0.1:8000/api/book/```

- **To get Book By ID**
   - Syntax : ```/api/book/id=<int:id>/```
   - Usage : ```127.0.0.1:8000/api/book/id=1/```

- **To get book by page number and size**
  - Syntax : ```/api/book/page=<int:page>/size=<int:size>/```
  - Usage : ```127.0.0.1:8000/api/book/page=1/size=5/```

- **To get first 10 reviews**
  - Syntax : ```/api/review/book=<int:bookid>/```
  - Usage : ```127.0.0.1:8000/api/review/book=1/```

- **To get reviews by page number and size**
  - Syntax : ```/api/review/book=<int:bookid>/page=<int:page>/size=<int:size>/```
  - Usage : ```127.0.0.1:8000/api/review/book=1/page=2/size=5/```
 
- **To search book through keyword. The default page size of search API is limit to 5. Increase page number to view more**
  - Syntax : ```/book/search?q="keyword"```
  - Syntax : ```/book/search?q="keyword"&page="Number"```
  - Usage : ```127.0.0.1:8000/book/searchq?q="python"&page="2"```

#### DELETE API
- **To Delete Book by id**
  - Syntax : ```/api/delete/book=<int:bookid>```
  - Usage : ```127.0.0.1:8000/api/delete/book=1```

#### POST API
- **To Add Book**
  - Syntax : ```/api/addbook/```
  - Usage : ``127.0.0.1:8000/api/addbook``
  - #### Required Parameters
    ```
    Header Parameter
     Content-Type = multipart/form-data
    
    Body Parameter
     "Title" = "Book Title"
     "Price" = "Book Price"
     "Type" = "Book Type 'Free' or 'Premium'"
     "Cover" = "Cover Image. Accepts Null too"
     "PDF" = "Book in Pdf format"
     "Description" = "Book Descrition or Abstract of book"
     "Category" = "Book Category"
     "UserID" = "Valid User ID"
    ```
  
#### PUT API
- **To Update Book by id**
  - syntax : ```/api/updatebook/id=<int:bookid>```
  - usage : ```127.0.0.1:8000/api/updatebook/id=1```
  - #### Required Parameters
    ```
    Body Parameter
     "title" = "Book Title"
     "price" = "Book Price"
     "booktype" = "Book Type 'Free' or 'Premium'"
     "description" = "Book Descrition or Abstract of book"
     "category" = "Book Category"
     "userid" = "Owner User ID"
    ```
