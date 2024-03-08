from django.db import models


# Create your models here.

class Book(models.Model):
    Title=models.CharField(max_length=80)
    Author=models.CharField(max_length=80)
    ISBN=models.IntegerField()
    Genre=models.CharField(max_length=80)
    Publication_date=models.DateField()

    def __str__(self):
        return self.Title


class User(models.Model):
    username=models.CharField(max_length=80)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)  # Assuming you store hashed passwords
    borrowed_books = models.ManyToManyField('Book', related_name='borrowed_by', blank=True)
    reserved_books=models.ManyToManyField('Book',related_name='reserved_by',blank=True)

    def __str__(self):
        return self.username
