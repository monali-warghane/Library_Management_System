from django.db import models

# Create your models here.
class AddBooks(models.Model):
    book_name = models.CharField(max_length=100)
    isbn = models.PositiveIntegerField()
    author = models.CharField(max_length=100)
    book_id = models.PositiveIntegerField()
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

class IssueBook(models.Model):
    stud_enroll_no = models.PositiveIntegerField()
    stud_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    book_id = models.PositiveIntegerField()
    issue_date = models.DateTimeField(auto_now=False)
    return_date = models.DateTimeField(auto_now=False)

    def __str__(self):
        return self.stud_name

class Returnbook(models.Model):
    stud_enroll_no = models.PositiveIntegerField()
    stud_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    book_name = models.CharField(max_length=100)
    book_id = models.PositiveIntegerField()
    return_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.stud_name


