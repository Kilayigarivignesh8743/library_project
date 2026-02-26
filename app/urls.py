from django.urls import path
from .views import home,register,login,login_validation,teachersDashboard,studentsDashboard,add_book,get_book,update_book,issue_book,return_book,delete_book,book_list_page,issue_book_page

urlpatterns = [
    path("",home),
    path("register/",register),
    path("login/",login),
    path("login_validation/",login_validation),
    
    path("studentsDashboard/<int:id>/",studentsDashboard),
    path("studentsDashboard/<int:id>/studentProfile/",studentsDashboard),
    path("studentsDashboard/<int:id>/availableBooks/",studentsDashboard),
    path("studentsDashboard/<int:id>/issuedBooks/",studentsDashboard),
    path("studentsDashboard/<int:id>/logout/",studentsDashboard),


    path("teachersDashboard/<int:id>/",teachersDashboard),
    path("teachersDashboard/<int:id>/studentProfile/",teachersDashboard),
    path("teachersDashboard/<int:id>/availableBooks/",teachersDashboard),
    path("teachersDashboard/<int:id>/issuedBooks/",teachersDashboard),
    path("teachersDashboard/<int:id>/logout/",teachersDashboard),
    

    path("add_book/",add_book),
    path("get_book/",get_book),
    path("update_book/<int:id>/",update_book),
    path("issue_book/<int:id>/",issue_book),
    path("return_book/<int:id>/", return_book),
    path("delete_book/<int:id>/",delete_book),
    path("books/", book_list_page),
    path("issue/", issue_book_page),


]
  
