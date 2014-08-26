# app/views.py
# Custom views

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


# Home
def home(request):
    if request.user.is_authenticated():
        return render(request, 'user.html')
    else:
        return render(request, 'home.html')


# User
@login_required(login_url='/login', redirect_field_name='user')
def user(request):
    if not request.user.is_authenticated():
        return redirect('/no_access')
    return render(request, 'user.html')

# Test
@login_required(login_url='/login', redirect_field_name='test')
def test_view(request):
    if not request.user.username=='TestRobot':
        return redirect('/no_access')
    return render(request, 'test.html')


# Forbidden
def no_access(request):
    return render(request, 'no_access.html')


# Log out
def logout_view(request):
    logout(request)
    return  redirect('/')
