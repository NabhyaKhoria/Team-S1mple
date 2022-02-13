from urllib import request
from django.shortcuts import render
from .models import *

# Create your views here.
def index(request):
    notices = Notice.objects.all()
    supervisers = Superviser.objects.all()
    print(supervisers)
    context = {
        'notices':notices,
    
    }
    return render(request,'index.html',context)


