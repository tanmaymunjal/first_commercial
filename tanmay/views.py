from asyncio.windows_events import NULL
from django.shortcuts import render
from django.contrib import admin
from datetime import datetime
from hello.models import Contact
from django.contrib import messages
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

def index(request):
    return render(request, 'initial.html') #returns the initial.html

def menu(request):
    return render(request,'menu.html')

def contact(request):
    if request.method=="POST":
        email=request.POST.get('email')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        feedback=request.POST.get('feedback')
        x=0
        try: 
            validate_email(email)
        except ValidationError as e:
             messages.error(request, 'Your feedback could not be sent, please check entered information.')
             x=x+1
        if x==0:
            if (email=="" or first_name=="" or last_name=="" or feedback=="" or email==NULL or first_name==NULL or last_name==NULL or feedback==NULL):
              messages.error(request, 'Your feedback could not be sent, please check entered information.')
            else:            
              contact=Contact(email=email,first_name=first_name,last_name=last_name,feedback=feedback,date=datetime.today())
              contact.save()
              messages.success(request, 'Your feedback has been shared.')


    return render(request,'contact.html')


