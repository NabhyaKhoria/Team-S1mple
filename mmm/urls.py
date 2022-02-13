from django.contrib import admin
from django.urls import path
from . import views
import mmm

app_name = 'mmm'

urlpatterns = [
    path('',views.index,name="home"),
    path('notice_detail/(?P<pk>[0-9a-f-]+)/$',views.notice_detail,name="notice_detail"),
]
