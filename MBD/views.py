from django.shortcuts import render
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

def index(request):
        return render(request,'MBD/home.html')
#    return HttpResponse(template.render(request, 'first/home.html'))
