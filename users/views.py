from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import Usereditform, Profileeditform
from posts.models import Post
from datetime import time

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user is not None:
                login(request, user)
                return redirect('feed')
            else:
                return HttpResponse('invalid credentials')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {"form": form})

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def index(request):
    current_user = request.user
    user_posts = Post.objects.filter(user=current_user)
    profile = Profile.objects.filter(user=current_user).first()
    return render(request, 'users/index.html', {"user_posts":user_posts, "profile":profile})

def RegisterPage(request):
    form = RegisterForm()
    if request.method == "POST":
        user_form = RegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            Profile.objects.create(user=new_user)
            return render(request, "users/register_done.html")
    else:
        user_form = RegisterForm()
    return render(request, "users/register.html", {"user_form":user_form})

@login_required
def edit(request):
    if request.method == "POST":
        user_form = Usereditform(instance = request.user, data=request.POST)
        profile_form = Profileeditform(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render("index")
                    
    else:
        user_form = Usereditform(instance = request.user)
        profile_form = Profileeditform(instance=request.user.profile, files=request.FILES)
        
    return render(request, "users/edit.html", {"user_form":user_form, "profile_form":profile_form})
        