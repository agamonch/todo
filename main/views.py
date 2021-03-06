from django.shortcuts import render, HttpResponse, redirect
from .models import ToDo, BookShop
# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    todo_list = ToDo.objects.all()
    return render(request, "test.html", {"todo_list": todo_list})

def index_1(request):
    return render(request, "index_1.html")

def index_2(request):
    return render(request, "index_2.html")
def index_3(request):
    return render(request, "index_3.html")
def books(request):
    bookshop_list = BookShop.objects.all()
    return render(request, "books.html", {"bookshop_list": bookshop_list})
def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = ToDo(text=text)
    todo.save()
    return redirect(test)

def add_book(request):
    form_1 = request.POST
    book_title = form_1["book_title"]
    author = form_1["author"]
    price = form_1["price"]
    bookshop = BookShop(book_title=book_title, author=author, price=price)
    bookshop.save()
    return redirect(books)
def delete_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)
def unmark_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)
def delete_books(request, id):
    bookshop = BookShop.objects.get(id=id)
    bookshop.delete()
    return redirect(books)
def mark_books(request, id):
    bookshop = BookShop.objects.get(id=id)
    bookshop.is_favorite1 = True
    bookshop.save()
    return redirect(books)
def unmark_books(request, id):
    bookshop = BookShop.objects.get(id=id)
    bookshop.is_favorite1 = False
    bookshop.save()
    return redirect(books)
def close_todo(request, id):
    todo = ToDo.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)
def details(request, id):
    bookshop_list = BookShop.objects.get(id=id)
    return render(request, "books_detail.html", {"bookshop_list": bookshop_list})
