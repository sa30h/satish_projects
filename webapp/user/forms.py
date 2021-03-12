from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Worker
from django import forms


class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}

class WorkerSignUpForm(forms.ModelForm):
    class Meta:
        model:Worker
        fields=['username','firstname','lastname','email','password']