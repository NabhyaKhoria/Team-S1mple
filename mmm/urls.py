from django.contrib import admin
from django.urls import path
from . import views
import mmm

app_name = 'mmm'

urlpatterns = [
    path('',views.index,name="home"),
]
