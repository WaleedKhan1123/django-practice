from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required

name = 'waleed'

def home(request):
    return render(request,'home/welcome.html',{'today': datetime.today()})

@login_required(login_url='/admin')
def autorhized(request):
    return render(request,'home/authorized.html',{})