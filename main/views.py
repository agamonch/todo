from django.shortcuts import render, HttpResponse
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
