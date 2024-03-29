from django.shortcuts import render, redirect
from main_pages.forms import *
from django.contrib.auth import logout
from main_pages.services import *
from django.http import HttpResponse
import json


def logout_user(request):
    logout_user_account(request)
    return redirect("home_page")


def home(request):
    return render(request, 'main_pages/index.html')


def ide(request):
    return render(request, 'main_pages/ide.html')


def course(request):
    return render(request, 'main_pages/course.html')


def user_login(request):

    form = LoginForm(request.POST if request.POST else None)
    form = user_authorization(request, form)

    context = {
        'form': form,
    }

    if form == True:
        return redirect('home_page')
    
    return render(request, 'main_pages/login.html', context)


def regist(request):

    form = CustomUserForm(request.POST if request.POST else None)
    context = user_registration(request, form)

    if context == True:
        return redirect('home_page')

    return render(request, 'main_pages/regist.html', context)


def task(request, task_number):

    context = task_handler(request, task_number)

    return render(request, f'main_pages/task{task_number}.html', context)
