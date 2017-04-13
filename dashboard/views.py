from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .members_form import MembersForm
from .checkin_form import MembersCheckinForm
from .models import *

from utils import PaymentGenerator


@login_required
def index(request):
    gym_list = Gym.objects.all()
    plan = GymPlan.objects.all()
    payment = PaymentPeriod.objects.all()
    activity = GymActivity.objects.all()
    team = FightTeam.objects.all()
    context = {
        'gym_list': gym_list,
        'gym_number': len(gym_list),
        'plan_list': plan,
        'payment_list': payment,
        'acitiviy_list': activity,
        'team_list': team,
    }
    return render(request, 'dashboard/sbadmin/pages/index.html', context)


@login_required
def gymadmin(request):
    gym_list = Gym.objects.all()
    context = {'gym_list': enumerate(gym_list, start=1), 'gym_number': len(gym_list)}
    return render(request, 'dashboard/sbadmin/pages/gymadmin.html', context)


@login_required
def members(request):
    query = request.GET.get("q", None)
    member_list = Members.objects.all()
    if query is not None:
        member_list = member_list.filter(
            Q(vorname__icontains=query) |
            Q(name__icontains=query) |
            Q(street1__icontains=query) |
            Q(email_name__icontains=query)
        )

    context = {
        'members': member_list,
        'count': len(member_list),
    }
    return render(request, 'dashboard/sbadmin/pages/members.html', context)


@login_required
def members_detail(request):
    member_list = Members.objects.get(id=request.GET['id'])
    gym_list = Gym.objects.all()
    plan = GymPlan.objects.all()
    payment = PaymentPeriod.objects.all()
    activity = GymActivity.objects.all()
    team = FightTeam.objects.all()
    context = {
        'gym_list': enumerate(gym_list, start=1),
        'gym_number': len(gym_list),
        'plan_list': enumerate(plan, start=1),
        'payment_list': payment,
        'acitiviy_list': activity,
        'team_list': team,
        'members': member_list,
    }
    return render(request, 'dashboard/sbadmin/pages/members_detail.html', context)


@login_required
def members_add(request):
    if request.method == 'POST':
        form = MembersForm(request.POST, request.FILES)
        print request.FILES['member_pic']
        if form.is_valid():
            form.save()
            m = Members.objects.get(uuid=form.cleaned_data['uuid'])
            # auto generate the payment record from the join date to current date
            PaymentGenerator.generateRecord()
            return HttpResponseRedirect('members')
        else:
            print form.errors
    else:
        form = MembersForm()

    gym_list = Gym.objects.all()
    plan = GymPlan.objects.all()
    payment = PaymentPeriod.objects.all()
    activity = GymActivity.objects.all()
    team = FightTeam.objects.all()
    context = {
        'gym_list': enumerate(gym_list, start=1),
        'gym_number': len(gym_list),
        'form:': form,
        'plan_list': enumerate(plan, start=1),
        'payment_list': payment,
        'acitiviy_list': activity,
        'team_list': team
    }
    return render(request, 'dashboard/sbadmin/pages/add_member.html', context)


@login_required()
def members_delete(request):
    Members.objects.get(id=request.GET['id']).delete()
    return HttpResponseRedirect('members')


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


@login_required
def members_checkin(request):
    if request.method == 'POST':
        form = MembersCheckinForm(request.POST)
        if form.is_valid():
            # check if gym_id exists in user table
            try:
                member = Members.objects.get(uuid=request.POST['gym_id'])
            except ObjectDoesNotExist:
                member = None

            if member is not None:
                form.save()
                return HttpResponseRedirect('checkin')
            else:
                form.add_error("gym_id", "Gym ID does not exists! Please enter again.")
            # if form.has_error:
            #     data = form.errors.iteritems()
            #     for key, value in data:
            #         error_str = "{field}: {error}".format(
            #             field=key,
            #             error=value.as_text()
            #         )
            #         print error_str
        else:
            print form.errors

    else:
        form = MembersCheckinForm()

    return render(request, 'dashboard/sbadmin/pages/checkin.html', {'form': form})


@login_required
def members_viewcheckin(request):
    current_members = GymCheckin.objects.filter(status=1)
    id_list = []
    for member in current_members:
        id_list.append(member.gym_id)
    member = Members.objects.filter(uuid__in=id_list)
    context = {
        "member_list": member,
        "total_members": len(current_members)
    }
    return render(request, 'dashboard/sbadmin/pages/view_checkin.html', context)


@login_required
def payment_record(request):
    # TODO: change this into a cron job
    PaymentGenerator.generateRecord()
    payment_list = PaymentRecord.objects.all()
    context = {
        'payments': payment_list,
        'count': len(payment_list),
    }
    return render(request, 'dashboard/sbadmin/pages/payments.html', context)


@login_required
def payment_record_change_status(request):
    payment_obj = PaymentRecord.objects.get(id=request.GET['id'])
    print("status: ", payment_obj.pay_status)
    if payment_obj.pay_status is False:
        payment_obj.pay_status = True
    else:
        payment_obj.pay_status = False
    payment_obj.save()
    return HttpResponseRedirect('payments')
    pass
