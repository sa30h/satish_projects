from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def contacts(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        feedback=request.POST.get('feedback')
        contact=Contact(name=name,email=email,mobile=mobile,feedback=feedback,date=datetime.today())
        contact.save()
        messages.success(request,"profile details updated")
    return render(request,'contacts.html')
def services(request):
    return render(request,'services.html')