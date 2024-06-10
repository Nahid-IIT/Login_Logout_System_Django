from django.shortcuts import render,redirect
from first_app import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import login,logout,authenticate,update_session_auth_hash
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method =="POST":
        register_form = forms.RegisterForm(request.POST)
        if register_form.is_valid():
            messages.success(request, 'Registration Successfull')
            register_form.save()
            return redirect('login')
    else:
        register_form = forms.RegisterForm()
    return render(request, 'register.html', {'form':register_form, "type": "Registstion"})
            

def user_login(request):
    if request.method == 'POST':
        login_form = AuthenticationForm(request=request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request, "Login successfull")
                return redirect('profile')
            else: 
                pass
        else:
            messages.success(request, 'No user found')
    else:
        login_form = AuthenticationForm()
    return render(request, 'register.html', {'form': login_form, "type": "Login"})

@login_required(login_url="/login/")            
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='/login/')
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required(login_url="/login/") 
def change_password_without_old(request):
    if request.method =='POST':
        form = SetPasswordForm(user = request.user, data = request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
    else:
        form = SetPasswordForm(user = request.user)
    return render(request, 'register.html', {'form': form})


@login_required(login_url="/login/") 
def change_password_with_old(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, "Password Changed successfully")
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request,'register.html', {"form":form, "type":"Change Password"})