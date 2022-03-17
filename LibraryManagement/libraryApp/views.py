from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render,redirect
from .forms import BookForm
from .models import Books

# Create your views here.


def book_list(request):
    context={'booklist':Books.objects.all()
             }
    return render(request,"libraryapp/book_list_card.html",context)

def add_books(request,id=0):
    if request.method=="GET":
        if id==0:
            form=BookForm()
            print(form)
        else:
            book=Books.objects.get(pk=id)
            print(book)
            form=BookForm(instance=book)
            print(form)
        return render(request,"libraryapp/add_books.html",{'form':form})

    else:
        if id==0:
            form=BookForm(request.POST)
        else:
            book=Books.objects.get(pk=id)
            form=BookForm(request.POST,instance=book)
        if form.is_valid():
            form.save()
        return redirect('book_list')






def delete_books(request,id):
    book=Books.objects.get(pk=id)
    book.delete()
    return redirect("book_list")

