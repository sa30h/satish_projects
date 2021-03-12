from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout
from .forms import SignUpForm,WorkerSignUpForm

# Create your views here.
def home(request):
    return render(request,'user/home.html')

def userSignup(request):
    if request.method=="POST":
        fm=SignUpForm(request.POST)
        if fm.is_valid():
            fm.save()
            return HttpResponseRedirect('/home/')
    else:
        fm=SignUpForm()
    return render(request,'user/usersignup.html',{'form':fm})

def userLogin(request):
    if request.method == "POST":
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            uname=fm.cleaned_data['username']
            upass=fm.cleaned_data['password']
            user=authenticate(username=uname,password=upass)
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/home/')

    else:
        fm=AuthenticationForm()
    return render(request,'user/userlogin.html',{'form':fm})

def workerSignUp(request):
    fm=WorkerSignUpForm()
    return render(request,'user/workerSignUp.html',{'form':fm})
