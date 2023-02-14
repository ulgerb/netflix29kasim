from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.


def loginUser(request):
    context = {}

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('profilUser')
    
    
    return render(request,'users/login.html',context)


def registerUser(request):
    context = {}

    if request.method == "POST":
        name = request.POST["name"]
        surname = request.POST["surname"]
        email = request.POST["email"]
        username = request.POST["username"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]
        
        if password1 == password2:
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=username, 
                                                    password=password1,
                                                    email=email,
                                                    first_name=name,
                                                    last_name=surname)
                    user.save()
                    return redirect("loginUser")
                    
    
    return render(request, 'users/register.html', context)


def AccountUser(request):
    context = {}
    return render(request, 'users/hesap.html', context)


def profilUser(request):
    context = {}
    return render(request, 'users/browse.html', context)
