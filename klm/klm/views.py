from django.shortcuts import render

def home(request):
    return render(request,'klm/home.html')