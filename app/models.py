from django.db import models

# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    status = models.CharField(max_length=30, default="Available")


    def __str__(self):
        return self.title
    

class Teacher(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    teacher_id=models.CharField(max_length=20)
    dept=models.CharField(max_length=30)
    ph_num=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    c_password=models.CharField(max_length=15)
    role=models.CharField(max_length=15)
    

    def __str__(self):
        return self.name


class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(unique=True)
    student_id=models.CharField(max_length=20)
    dept=models.CharField(max_length=30)
    ph_num=models.CharField(max_length=15)
    password=models.CharField(max_length=15)
    c_password=models.CharField(max_length=15)
    role=models.CharField(max_length=15)
    

    def __str__(self):
        return self.name


