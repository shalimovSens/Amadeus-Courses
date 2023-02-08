from django.shortcuts import render, redirect
from .forms import *
from django.contrib.auth import authenticate, login, logout
from .services import handle_special_task

def logout_user(request):
    logout(request)
    return redirect("home_page")


def home(request):
    return render(request, 'main_pages/index.html')


def ide(request):
    return render(request, 'main_pages/ide.html')


def course(request):
    return render(request, 'main_pages/course.html')


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            global id
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('home_page')
            else:
                form.message = 'Неверный логин или пароль.'
    else:
        form = LoginForm()
    return render(request, 'main_pages/login.html', {'form': form})


def regist(request):
    form = CustomUserForm(request.POST if request.POST else None)
    if form.is_valid():
        user = form.save()
        user.set_password(user.password)
        user.confirm_password = ''
        user.progress = []
        user.pos = len(CustomUser.objects.all()) - 1
        user.save()
        login(request, user)
        return redirect('home_page')
    context = {
        'form': form
    }
    return render(request, 'main_pages/regist.html', context)


def task_handler(request, task_number, special_task=1):
    if task_number == special_task:
        form = None
        context = handle_special_task(form)
        if context:
            return render(request, f'main_pages/task{special_task}.html', context)
        else:
            return redirect('login')
    else:
         return render(request, f'main_pages/task{task_number}.html')

