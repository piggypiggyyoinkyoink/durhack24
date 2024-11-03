from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth import models, authenticate, logout
from django.contrib.auth.models import User as Auth_User
from .models import *
from django.urls import reverse
import datetime, random#, pillow
from django.contrib.auth import hashers
from django.db.models import Q
#from icecream import ic
from django.contrib.auth import update_session_auth_hash, login
# Create your views here.

def home(request):
    template = loader.get_template("home.html")
    context = {

    }

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
            user = Auth_User.objects.create_user(username=email, email=email, password=password)
            user.first_name = fname
            user.last_name = lname
            user.save()
            userProfile = User(email = email, password = hashers.make_password(password), first_name = fname, last_name = lname, bio=bio, pronouns=pronouns)
            userProfile.save()
            return redirect('/')
        else:
            return redirect("/signup")


def loginPage(request):
    template = loader.get_template("login.html")
    context = {}
    return HttpResponse(template.render(context, request))

def loginProcessing(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(username = email, password = password)
        if user is not None:
            login(request, user)
            return redirect('/search')
        else:
            return redirect("/login")

def createGroup(request):
    template = loader.get_template("createGroup.html")
    context = {}
    return HttpResponse(template.render(context, request))

def createGroupProcessing(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        group = Group(name = title, description = description)
        group.save()
        return redirect('/search')
    
def test(request):
    data = request.POST.get('text')
    groups = Group.objects.filter(name__icontains = data).values_list()
    response = HttpResponse()
    t = len(groups)
    if t %2 != 0:
        t+=1
    print(groups)
    for group in groups:
        if t % 2 == 0 :
            response.write("<div class = 'row'>")
        response.write("<div class='col'> <div class='groupCard' <h3>" + group[1] + "</h3> <p>" + group[2] + "</p> </div> </div>")
        if t % 2 == 1:
            response.write("</div>")
        t -= 1
    if t %2 == 1:
        response.write("<div class = 'col'> </div></div>")
    return response