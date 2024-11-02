from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import models
from django.contrib.auth.models import User
from .models import *
from django.urls import reverse
import datetime, random
from django.contrib.auth import hashers
from django.db.models import Q
#from icecream import ic
from django.contrib.auth import update_session_auth_hash, login
# Create your views here.

def home(request):
    template = loader.get_template("home.html")
    context = {}

    return HttpResponse(template.render(context, request))

def search(request):
    template = loader.get_template("search.html")
    context = {}
    return HttpResponse(template.render(context, request))

<<<<<<< HEAD
def signUp(request):
    template = loader.get_template("signUp.html")
    context = {}
    return HttpResponse(template.render(context, request))

=======
>>>>>>> a8ab155c409880cace94b020cbba8ac2369d283e
def about(request):
    return render(request, 'about.html')