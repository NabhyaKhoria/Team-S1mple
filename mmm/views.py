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
    return render(request,'index2.html',context)

def notice_detail(request,pk):
    notice = Notice.objects.filter(id=pk)
    print(notice)
    context = {
        'notice':notice,
    }
    return render(request,'portfolio-details.html',context)


