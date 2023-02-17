from django.shortcuts import render,get_object_or_404, redirect, HttpResponseRedirect
from appUser.models import *
from appMy.models import *

# Create your views here.


def index(request):
    context = {"title":"Netflix"}
    return render(request,'index.html',context)

def browseIndex(request,id):
    context = {"title": "Netflix - Browse"}
    profil = get_object_or_404(Profil,id=id)
    videos = Video.objects.all()
    
    context.update({"profil": profil, "videos": videos})
    return render(request,'browse-index.html',context)

def likeIndex(request,pid,vid):
    profil = Profil.objects.get(id=pid)
    video = Video.objects.get(id=vid)
    likevideo = LikeVideo.objects.filter(profil=profil, video=video)
    if not likevideo.exists():
        like = LikeVideo(profil=profil, video=video)
        like.save()
    else:
        likevideo.delete()
        
    return HttpResponseRedirect("/netflix/"+pid+"/")