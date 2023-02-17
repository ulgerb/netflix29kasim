from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import *

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
                else:
                    context.update({"hata":"Bu Email adresi zaten kullanılıyor!"})
            else:
                context.update({"hata": "Bu kullanıcı adı zaten kullanılıyor!"})
        else:
            context.update({"hata": "Şifreler aynı değil!"})
    
    return render(request, 'users/register.html', context)


def AccountUser(request):
    context = {}
    return render(request, 'users/hesap.html', context)


def profilUser(request):
    context = {}
    profils = Profil.objects.filter(user=request.user)
    print(len(list(profils)))
    if not (len(list(profils)) >=4):
        if request.method == "POST":
            name = request.POST["name"]
            image = request.FILES["image"]
            
            profil = Profil(name = name, image = image, user=request.user)
            profil.save()
            return redirect('profilUser')
    else:
        context.update({"max_profils":True})
    context.update({"profils": profils})
    return render(request, 'users/browse.html', context)

def profilUserDelete(request,id):
    profil = Profil.objects.get(id=id)
    profil.delete()
    return redirect('profilUser')
