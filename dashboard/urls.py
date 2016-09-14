from django.conf.urls import url

from . import views
from . import login_views

urlpatterns = [
    # ex: /polls/
    url(r'^login$', login_views.login, name='login'),
    url(r'^logout$', login_views.logout, name='logout'),
    url(r'^login_check$', login_views.login_check, name='login_check'),
    #
    url(r'^$', views.index, name='index'),
    url(r'^index$', views.index, name='index'),
    url(r'^tables$', views.tables, name='tables'),
    url(r'^forms$', views.forms, name='forms'),
    url(r'^members/add_members$', views.members_add, name='members_add'),
    url(r'^members/edit$', views.members_edit, name='members_edit'),
    # ex: /polls/5/
    url(r'^(?P<gym_id>[0-9]+)/gym/$', views.gym, name='gym'),
    # ex: /polls/5/results/
    url(r'^(?P<member_id>[0-9]+)/member/$', views.member, name='member'),
]
