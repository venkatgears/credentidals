from json.encoder import JSONEncoder
from django import forms
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from .forms import Userforms
from .models import Register
from django.urls import reverse

# Create your views here.


def home_view(request):

    return render(request, "credentials/home.html", {})


def create_view(request):
    if request.method == "POST":
        form = Userforms(request.POST)
        if form.is_valid():
            form.save()
            a = form.save()

            return render(request, "credentials/home.html", {"name": a.name})

        else:
            return JsonResponse(
                status=404,
                data={"status": "data not valid", "message": "information not valid"},
            )
    form = Userforms()
    return render(request, "credentials/index.html", {"form": form})


def show_users(request):
    if request.method == "POST":
        username = request.POST.get("username")
        obj = Register.objects.filter(name=username)
        context = {
            "name": obj[0].name,
            "email": obj[0].email,
        }

        return JsonResponse(context)
    else:
        return render(request, "credentials/showusers.html", {})
