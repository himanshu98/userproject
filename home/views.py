from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth import  login as auth_login
from django.contrib.auth import  logout as auth_logout
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    return render(request,'login.html')

def login(request):
    if request.method == 'POST':
        loginusername=request.POST['username']
        loginpassword=request.POST['password']

        user=authenticate(username=loginusername,password=loginpassword)

        if user is not None:
            auth_login(request,user)
            messages.success(request,"Successfully logged in")
            return redirect('home')
        else:
            messages.error(request,"Invalid credentials please try again")
            return redirect('home')

def logout(request):
        auth_logout(request)
        messages.success(request,"Successfully logged out")
        return redirect('home')

def signup(request):
    if request.method == 'POST':
        #get the user parameter
        username=request.POST["username"]
        fname=request.POST["fname"]
        lname=request.POST["lname"]
        email=request.POST["email"]
        pass1=request.POST["pass1"]
        pass2=request.POST["pass2"]
        username=request.POST["fname"] 

        #check for erroneous  inputs
        #user name should be under 10 characters
        if len(username) > 10:
            messages.error(request,"username must be under 10 characters")
            return redirect('home')
        # username should be alphanumuneric
        if not username.isalnum():
            messages.error(request,"username should contain only letters and numbers")
            return redirect('home')
        
        if pass1!=pass2:
            messages.error(request,"passwords do not match")
            return redirect('home')


        #Create the user
        myuser=User.objects.create_user(username,email,pass1)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.success(request,"Your account has been succesfully created!!")
        return redirect('home')
    else:
        return HttpResponse('404-NOT FOUND')
