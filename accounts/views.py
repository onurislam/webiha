from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def LoginView(request):
    if not request.user.is_authenticated:
        form = LoginForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                try:
                    username = form.cleaned_data.get('username')
                    password = form.cleaned_data.get('password')
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/panel/')
                except:
                    return render(request, 'account/login.html', {'form': form, 'error': 'Username OR Password Error'})

        return render(request, 'account/login.html', {'form': form, 'error': ""})
    else:
        return redirect('/panel/')


def RegisterView(request):
    if not request.user.is_authenticated:
        form = RegisterForm(request.POST or None)
        if request.method == "POST":
            if form.is_valid():
                try:
                    if form.cleaned_data.get('password') == form.cleaned_data.get('passwordAgain'):
                        user = User.objects.create_user(form.cleaned_data.get('username'), 'a@a.com',
                                                        form.cleaned_data.get('password'))
                        user.save()
                        return redirect('login')
                    else:
                        return render(request, 'account/register.html', {'form': form, 'error': 'Password Error'})
                except:
                    return render(request, 'account/register.html', {'form': form, 'error': 'Username Error!'})

        return render(request, 'account/register.html', {'error': ""})
    else:
        return redirect('/panel/')


def Logout(request):
    logout(request)
    return redirect('login')
