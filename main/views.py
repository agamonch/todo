from django.shortcuts import render, HttpResponse

# Create your views here.
def homepage(request):
    return render(request, "index.html")

def test(request):
    return render(request, "test.html")

def index_1(request):
    return render(request, "index_1.html")

def index_2(request):
    return render(request, "index_2.html")
def index_3(request):
    return render(request, "index_3.html")