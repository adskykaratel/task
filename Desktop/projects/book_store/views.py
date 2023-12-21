from django.shortcuts import render
from django.http import JsonResponse
from .models import Book

def book_list_api(request):
    books = Book.objects.all()
    data = {'books':list(books.values())}
    return JsonResponse(data, safe=False)

# Create your views here.
