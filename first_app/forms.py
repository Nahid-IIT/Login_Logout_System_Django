from django.db import models
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class RegisterForm(UserCreationForm):
    first_name  = forms.CharField(widget=forms.TextInput(attrs ={'id':'required'}))
    last_name  = forms.CharField(widget=forms.TextInput(attrs ={'id':'required'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'id':'required'}))
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

