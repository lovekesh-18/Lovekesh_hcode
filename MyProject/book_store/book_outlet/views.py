from django.shortcuts import render,get_object_or_404
from .models import *
from django.http import Http404
from django.db.models import Avg
# Create your views here.

def index(request):
    books = Book.objects.all().order_by("rating")
    cnt = books.count()
    average = books.aggregate(Avg("rating"))
    return render(request,'book_outlet/index.html',{
        'books': books,
        'cnt':cnt,
        'avg' : average
    })

def detail_page(request,slug):
    #book = get_object_or_404(Book,id=id)
    try:
        book = Book.objects.get(slug=slug)
    except:
        raise Http404()
    return render(request,'book_outlet/book_details.html',{
        'title' : book.title,
        'author' : book.author,
        'is_bestselling' : book.is_bestselling
    })