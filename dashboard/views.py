from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from .members_form import MembersForm
from .models import Gym


@login_required
def index(request):
    gym_list = Gym.objects.all()
    context = {
        'gym_list': gym_list,
        'gym_number': len(gym_list),
    }
    return render(request, 'dashboard/sbadmin/pages/index.html', context)


@login_required
def tables(request):
    return render(request, 'dashboard/sbadmin/pages/tables.html')


@login_required
def forms(request):
    return render(request, 'dashboard/sbadmin/pages/forms.html')


@login_required
def members_add(request):
    if request.method == 'POST':
        form = MembersForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('add_members')
        else:
            print form.errors
    else:
        print "leider, didn't even post"
        form = MembersForm()

    gym_list = Gym.objects.all()
    context = {'gym_list': enumerate(gym_list, start=1), 'gym_number': len(gym_list), 'form:': form}
    return render(request, 'dashboard/sbadmin/pages/add_members.html', context)


@login_required
def members_edit(request):
    return render(request, 'dashboard/sbadmin/pages/edit_members.html')


@login_required
def gym(request, gym_id):
    response = "You're looking at gym %s."
    return HttpResponse(response % gym_id)


@login_required
def member(request, member_id):
    response = "You're looking at member %s."
    return HttpResponse(response % member_id)
