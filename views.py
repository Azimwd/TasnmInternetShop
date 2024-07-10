from django.shortcuts import render

from app.users.forms import UserLoginForm


def login(request):
    form = UserLoginForm()
    context={
        'form': 
    }
    return render(request,'users/login.html', context)