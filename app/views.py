from django.shortcuts import render,redirect
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Book,Teacher,Student
# Create your views here.

# def home(req):
#     return HttpResponse("Home View")  //I mean naku nen register ane file call cheste bowser lo registarion di output ravali dini dvara

# html registration:
def home(req):
    return render(req,"register.html")



# Html book page
def book_list_page(request):
    books = Book.objects.all()
    return render(request, "book_list.html", {"books": books})



# Html issue page 
def issue_book_page(request):
    books = Book.objects.all()
    return render(request, "issue_book.html", {"books": books})




# teachers dashboard html file:
def teachersDashboard(req,id):
    teacher=Teacher.objects.get(id=id)
    issued_books = Book.objects.filter(status="Issued")
    if req.path == f"/teachersDashboard/{id}/":
        return render(req,"teachersDashboard.html",{"user":teacher,"issued_books":issued_books,"count":issued_books.count()})
    elif "studentProfile" in req.path:
        return render(req,"t_studentProfile.html",{"user":teacher})
    elif "availableBooks" in req.path:
        books = Book.objects.filter(status="Available")
        return render(req,"book_list.html",{"user":teacher,"books":books})
    elif "issuedBooks" in req.path:
        books = Book.objects.filter(status="Issued")
        return render(req,"t_issuedBooks.html",{"user":teacher,"books":issued_books})
    elif "logout" in req.path:
        return redirect("/login/")
    else:
        return render(req,"teachersDashboard.html",{"user":teacher})




 
# student dashboard html file:
def studentsDashboard(req,id):
        student = Student.objects.get(id=id)
        books_taken = Book.objects.filter(status="Issued")
        if req.path == f"/studentsDashboard/{id}/":
             return render(req,"studentsDashboard.html",{"user":student,"books_taken":books_taken})
        elif "studentProfile" in req.path:
             return render(req,"s_studentProfile.html",{"user":student})
        elif "availableBooks" in req.path:
            books = Book.objects.filter(status="Available")
            return render(req,"book_list.html",{"user":student,"books":books})
        elif "issuedBooks" in req.path:
            books = Book.objects.filter(status="Issued")
            return render(req,"s_issuedBooks.html",{"user":student,"books":books_taken})
        elif "logout" in req.path:
            return redirect("/login/")
        else:
            return render(req,"studentsDashboard.html",{"user":student})
      




@api_view(["POST"])
def register(req):

    n = req.data.get("n")
    e = req.data.get("e")
    i = req.data.get("i")
    d = req.data.get("d")
    ph = req.data.get("ph")
    p = req.data.get("p")
    cp = req.data.get("cp")
    r = req.data.get("r")


    #Password check
    if p != cp:
        return Response({"msg":"Password not matched"})

    #Email already exists check
    if r == "Teacher":
        if Teacher.objects.filter(email=e).exists():
            return Response({"msg":"Email already registered"})


    if r == "Student":
        if Student.objects.filter(email=e).exists():
            return Response({"msg":"Email already registered"})

    #Create user
    if r == "Teacher":

        Teacher.objects.create(
            name=n,
            email=e,
            teacher_id=i,
            dept=d,
            ph_num=ph,
            password=p,
            c_password=cp,
            role=r
        )

        return Response({"msg":"Teacher entered successfully"})


    elif r == "Student":

        Student.objects.create(
            name=n,
            email=e,
            student_id=i,
            dept=d,
            ph_num=ph,
            password=p,
            c_password=cp,
            role=r
        )
        return Response({"msg":"Student Registered Successfully"})





# Html login file:
@api_view(["GET"])
def login(req):
    return render(req,"login.html")


# login validation api:
@api_view(["POST"])
def login_validation(req):
    e=req.data.get("e")
    p=req.data.get("p")
    r=req.data.get("r")
    teach=Teacher.objects.all().values()
    stu=Student.objects.all().values()
    for j in stu:
        if j["email"] == e and j["password"] == p:
            if r == "Student":
                return Response({"msg":"login successfull for student","r_url":"studentsDashboard","id":j["id"],"role":j["role"]})
        else:
            continue

    for i in teach:
        if i["email"] == e and i["password"] == p:
            if r == "Teacher":
                return Response({"msg":"login successfull for teacher","r_url":"teachersDashboard","id":i["id"],"role":i["role"]})
        else:
            continue
    return Response({"t":teach})        
    



















# ADD Book 
@api_view(["POST"])
def add_book(req):
    t = req.data.get("title")
    a = req.data.get("author_name")
    book = Book.objects.create(title=t,author_name=a,status="Available")
    return Response({
        "Msg" : "Book Added successfully","book" : {
        "id": book.id,
        "title": book.title,
        "author_name": book.author_name,
        "status": book.status
    }})


# GET Book
@api_view(["GET"])
def get_book(req):
    booksData = Book.objects.all().values()
    bookList = []
    for ch in booksData:
        bookList.append(ch)
    return Response({
  "msg": "Books fetched successfully",
  "data": [
    {
      "id": 1,
      "title": "Python Basics",
      "author_name": "Guido",
      "status": "Available"
    }
  ]
})


# UPDATE Book
@api_view(["PUT"])
def update_book(req,id):
    t = req.data.get("title")
    a = req.data.get("author_name")
    bookobj = Book.objects.get(id=id)
    bookobj.title=t
    bookobj.author_name=a
    bookobj.save()
    # return Response({"msg": "Book updated successfully"})
    return Response({
    "msg":"Book updated successfully",
    "book":{
        "id":bookobj.id,
        "title":bookobj.title,
        "author_name":bookobj.author_name
    }
})


# ISSUE Book
@api_view(["PUT"])
def issue_book(req,id):
    bookobj = Book.objects.get(id=id)
    bookobj.status = "Issued"
    bookobj.save()
    # return Response({"msg" : "Book issued successfully"})
    return Response({
    "msg":"Book issued successfully",
    "book_id":bookobj.id,
    "status":bookobj.status
})


# RETURN Book
@api_view(["PUT"])
def return_book(request, id):
    book = Book.objects.get(id=id)
    book.status = "Available"
    book.save()
    return Response({"msg":"Book returned successfully"})


# DELETE Book
@api_view(["DELETE"])
def delete_book(req,id):
    bookobj = Book.objects.get(id=id)
    bookobj.delete()
    return Response({"msg": "Book deleted successfully"})






