from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, url
from apps.pokes import views

urlpatterns = [
    url(r'^pokes/$', login_required(views.Dashboard.as_view(),login_url='/accounts/main'),name='pokes-dashboard'),
    url(r'^poke/(?P<id>\d+)$' , login_required(views.poke,login_url='/accounts/main'),name='poke-someone'),
]
