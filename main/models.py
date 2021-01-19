from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class BookShop(models.Model):
    book_title = models.TextField()
    subtitle = models.TextField()
    description = models.TextField()
    price = models.TextField()
    genre = models.TextField()
    author = models.TextField()
    year = models.DateField()
    date = models.TimeField(auto_now_add=True)


