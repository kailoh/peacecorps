# Create your views here.
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponse
def home(request):
    return render_to_response('map.html')


def register(request):
    if request.method == "GET":
        register_form = UserCreationForm()
        context = {
            "r_form": register_form
        }
        return render(request, "registrationform.html", context)
    elif request.method == "POST":
        form = UserCreationForm(request.POST)
        profession = request.POST.get("profession")
        if form.is_valid():
            new_user = form.save()
            if profession == "teacher":
                return HttpResponse("<html><body bgcolor='#082239'><h2><font color='white'>Welcome teacher! <a href='/' style='color:white'>Please click for map.</a></h2>");
            else:
                return HttpResponse("<html><body bgcolor='#082239'><h2><font color='white'>Welcome volunteer! <a href='/' style='color:white'>Please click for map.</a></h2>");
        else:
            context = {
                "r_form": form
            }
