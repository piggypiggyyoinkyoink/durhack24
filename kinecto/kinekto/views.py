from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import models
from django.contrib.auth.models import User as Auth_User
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

def signUp(request):
    template = loader.get_template("signUp.html")
    context = {}
    return HttpResponse(template.render(context, request))

def signUpProcessing(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        bio = request.POST["bio"]
        pronouns = request.POST["pro"]
        if password == confirmPassword:
            user = Auth_User.objects.create_user(username=email, email=email, password=hashers.make_password(password))
            user.first_name = fname
            user.last_name = lname
            user.save()
            userProfile = User(email = email, password = hashers.make_password(password), first_name = fname, last_name = lname, bio=bio, pronouns=pronouns)
            userProfile.save()
            return redirect('/')
        else:
            return redirect("/signup")


def about(request):
    return render(request, 'about.html')