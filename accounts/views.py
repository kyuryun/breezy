from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from home.models import MyUser
from .forms import *
from django.views.generic import TemplateView

from django.contrib import auth
from .forms import RegisterForm
from django.contrib.auth.hashers import check_password

# Create your views here.
def register(request):
    context = {}
    if request.method == 'POST':
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)

            # name = request.POST['username']
            # if MyUser.objects.filter(username=name).exists():
            #     return render(request, 'registration/register.html', {'error': '아이디 또는 비밀번호를 확인해주세요'})


            username = request.POST['username']
            original = MyUser.objects.filter(username=username)
            name = request.POST['first_name']
            email = request.POST['email']
            phone = request.POST['phone']

            if request.POST['password'] != request.POST['password2']:
                # return render(request, 'registration/register.html', {'form':user_form, 'error': '비밀번호와 비밀번호 확인 값이 다릅니다.'})
                return render(request, 'registration/signup_error.html')

            if request.POST['email'] == '':
                return render(request, 'registration/register.html',
                              {'form': user_form, 'error': '이메일을 입력해주세요.'})

            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'registration/register_done.html', {'new_user':new_user})
    else:
        user_form = RegisterForm()
    return render(request, 'registration/register.html', {'form':user_form})


def login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'registration/login.html', {'error': '아이디 또는 비밀번호를 확인해주세요'})
    else:
        return render(request, 'registration/login.html')


def logout_request(request):
    auth.logout(request)
    return redirect('/')
    return render(request, 'registration/login.html')


def find_id(request):
    if request.method == 'POST':
        user_form = FindIdForm(request.POST)
        if user_form.is_valid():
            try:
                name = request.POST['first_name']
                email = request.POST['email']
                user = MyUser.objects.filter(first_name=name, email=email)
                user = user[0]
                return render(request, 'registration/find_done.html', {'user':user})
            except:
                return render(request, 'registration/find_error.html')
    else:
        user_form = FindIdForm()
    return render(request, 'registration/find_id.html', {'form':user_form})


def my_page(request):
    context = {}
    if request.method == "POST":
        current_password = request.POST.get("origin_password")
        user = request.user
        if check_password(current_password, user.password):
            new_password = request.POST.get("password1")
            password_confirm = request.POST.get("password2")
            if new_password == password_confirm:
                user.set_password(new_password)
                user.save()
                auth.login(request, user)
                return redirect("/")
            else:
                context.update({'error': "새로운 비밀번호를 다시 확인해주세요."})
        else:
            context.update({'error': "현재 비밀번호가 일치하지 않습니다."})

    return render(request, "registration/my_page.html", context)