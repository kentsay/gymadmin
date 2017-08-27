from django.conf.urls import url

from . import views
from . import login_views

urlpatterns = [
    # For login/logout
    url(r'^login$', login_views.login, name='login'),
    url(r'^logout$', login_views.logout, name='logout'),
    url(r'^login_check$', login_views.login_check, name='login_check'),
    # For Gym admin
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^gymadmin', views.gymadmin, name='gymadmin'),
    url(r'^members$', views.members, name='members'),
    url(r'^members_detail$', views.members_detail, name='members_detail'),
    url(r'^members_delete$', views.members_delete, name='members_delete'),
    url(r'^add_member$', views.members_add, name='members_add'),
    url(r'^edit_member$', views.members_edit, name='members_edit'),
    url(r'^payments$', views.payment_record, name='payment_record'),
    url(r'^payments_change$', views.payment_record_change_status, name='payment_record_change_status'),
    url(r'^checkin$', views.members_checkin, name='members_checkin'),
    url(r'^viewcheckin$', views.members_viewcheckin, name='members_viewcheckin'),
    url(r'^income_report$', views.income_report, name='income_report'),
    url(r'^members_report$', views.members_report, name='members_members_report'),

    # ex: /polls/5/
    url(r'^(?P<gym_id>[0-9]+)/gym/$', views.gym, name='gym'),
    # ex: /polls/5/results/
    url(r'^(?P<member_id>[0-9]+)/member/$', views.member, name='member'),
]
