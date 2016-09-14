from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

def login(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/sbadmin/pages/index.html')
    else:
        return render(request, 'dashboard/sbadmin/pages/login.html')

def logout(request):
    auth_logout(request)
    return render(request, 'dashboard/sbadmin/pages/login.html')

def login_check(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        auth_login(request, user)
        print "success login"
        return render(request, 'dashboard/sbadmin/pages/index.html')
        # Redirect to a success page.
    else:
        context = {
            'errors': True,
            'messages': "login fail"
        }
        return render(request, 'dashboard/sbadmin/pages/login.html', context)
        # Return an 'invalid login' error message.
