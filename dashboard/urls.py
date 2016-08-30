from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    url(r'^login$', views.login, name='login'),
    url(r'^tables$', views.tables, name='tables'),
    url(r'^forms$', views.forms, name='forms'),
    # ex: /polls/5/
    url(r'^(?P<gym_id>[0-9]+)/gym/$', views.gym, name='gym'),
    # ex: /polls/5/results/
    url(r'^(?P<member_id>[0-9]+)/member/$', views.member, name='member'),
]
