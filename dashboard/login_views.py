from django.conf import settings

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.contrib.auth import (
    REDIRECT_FIELD_NAME, get_user_model, login as auth_login,
    logout as auth_logout, update_session_auth_hash,
)
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.http import is_safe_url

@sensitive_post_parameters()
@csrf_protect
@never_cache
def login(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/index')
    else:
        redirect_field_name = REDIRECT_FIELD_NAME
        redirect_to = request.POST.get(redirect_field_name,request.GET.get(redirect_field_name, ''))
        return render(request, 'dashboard/sbadmin/pages/login.html', {'redirect_to':redirect_to})

def logout(request):
    auth_logout(request)
    return redirect(login)

def login_check(request):
    redirect_field_name = REDIRECT_FIELD_NAME
    redirect_to = request.POST.get(redirect_field_name,request.GET.get(redirect_field_name, ''))

    # Ensure the user-originating redirection url is safe.
    if not is_safe_url(url=redirect_to, host=request.get_host()):
        redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)
    # Okay, security check complete. Log the user in.

    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        # Redirect to a success page.
        auth_login(request, user)
        if redirect_to:
            return redirect(redirect_to)
        else:
            return redirect('/dashboard/index')
    else:
        # Return an 'invalid login' error message.
        messages.error(request, 'Username or password didn\'t match. Please try again.')
        return redirect('login')
