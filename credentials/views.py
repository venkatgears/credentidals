from django import forms
from django.shortcuts import render
from .models import register
from .forms import Userforms
# Create your views here.


def homeView(request):
    return render(request , 'credentials/home.html' , {})

def createView(request):
    form = Userforms(request.POST or None)
    if form.is_valid() :
        form.save()

    context = {
        'form' : form
    }

    return render(request,'credentials/index.html' , context)

def show_users(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        obj = register.objects.filter(name = username)
        context = {
            "name" : obj 
        }
        
        return render(request ,'credentials/showusers.html', context  )
    else :
        return render(request ,'credentials/showusers.html',{} )