from django.shortcuts import render,redirect
from .forms import UserForm, DetailsForm
from .models import profile
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth import login, authenticate

def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        details_form = DetailsForm(request.POST)
        if (user_form.is_valid() and details_form.is_valid()):
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

            username = user_form.cleaned_data.get('username')
            raw_password = user_form.cleaned_data.get('password')
            prof = details_form.save(commit=False)
            prof.user = user

            if(request.FILES['dp']):
                prof.dp = request.FILES['dp']
            prof.save()
            user = authenticate(username = username,password = raw_password)
            login(request,user)
            return redirect('home')
        else: 
            return render(request,'accounts/signup.html',{'error': 'Something went wrong :)'})

    else:
        user_form = UserForm()
        details_form = DetailsForm()
        return render(request,'accounts/signup.html',{'user_form':user_form,'details_form': details_form})

def userprofile(request,username):
    user = get_object_or_404(User,username = username)
    return render(request,'accounts/profile.html',{'user':user})