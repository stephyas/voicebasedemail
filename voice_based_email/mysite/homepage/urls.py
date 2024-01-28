from django.urls import re_path, include
from . import views

app_name = 'homepage'

urlpatterns = [
    re_path(r'^$', views.login_view, name="login"),
    re_path(r'^compose/$', views.compose_view, name="compose"),
    re_path(r'^inbox/$', views.inbox_view, name="inbox"),
    re_path(r'^sent/$', views.sent_view, name="sent"),
    re_path(r'^trash/$', views.trash_view, name="trash"),
    re_path(r'^options/$', views.options_view, name="options")
   
]
