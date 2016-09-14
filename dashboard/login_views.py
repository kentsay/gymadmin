from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages

def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/index')
    else:
        return render(request, 'dashboard/sbadmin/pages/login.html')

def logout(request):
    auth_logout(request)
    return redirect(login)

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # Redirect to a success page.
        auth_login(request, user)
        print "success login"
        return redirect('/dashboard/index')

    else:
        # Return an 'invalid login' error message.
        messages.error(request, 'Username or password didn\'t match. Please try again.')
        return redirect('login')
