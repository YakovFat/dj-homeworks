from django.shortcuts import render, redirect
from django.views.generic import FormView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

def home(request):
    return render(
        request,
        'home.html'
    )


def signup(request):
    return render(
        request,
        'signup.html'
    )


def my_login(request):
    form = User
    # if request.method == 'POST':
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(request, username=username, password=password)
    #     form = user
    #     if user is not None:
    #         login(request, user)
    #         return redirect('/')
    #     else:
    #         # Return an 'invalid login' error message.
    #         pass
    return render(
        request,
        'login.html',
        {'form': form}
    )
