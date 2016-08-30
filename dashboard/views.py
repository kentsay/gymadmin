from django.shortcuts import render
from django.http import HttpResponse

from .models import Gym

def index(request):
    gym_list = Gym.objects.order_by('name')[:5]
    context = {
        'gym_list': gym_list,
        'gym_number': len(gym_list),
    }
    return render(request, 'dashboard/sbadmin/pages/index.html', context)

def login(request):
    return render(request, 'dashboard/sbadmin/pages/login.html')

def tables(request):
    return render(request, 'dashboard/sbadmin/pages/tables.html')

def forms(request):
    return render(request, 'dashboard/sbadmin/pages/forms.html')



def gym(request, gym_id):
    response = "You're looking at gym %s."
    return HttpResponse(response % gym_id)

def member(request, member_id):
    response = "You're looking at member %s."
    return HttpResponse(response % member_id)
