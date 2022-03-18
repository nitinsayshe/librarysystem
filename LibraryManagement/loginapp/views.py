from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib import messages

from .forms import SignUpForm


def home(request):
    return render(request, 'home.html')

# def login(request):
#     if request.method=='POST' :
#         form=AuthenticationForm(data=request.POST)
#         if form.is_valid():
#             user=form.get_user()
#             login(request,user)
#             return redirect('book_list')
#     else:
#         form=AuthenticationForm()
#     return render(request,'loginapp/login.html',{"form":form})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            # raw_password = form.cleaned_data.get('password1')
            # user = authenticate(username=user.username, password=raw_password)
            # login(request, user)

            return redirect('login')
            #return render(request,'libraryapp/book_list_card.html')
    else:
        form = SignUpForm()
    return render(request, 'loginapp/signup.html', { 'form' : form })