from django.shortcuts import render

# Create your views here.


def index(request):
    context = {"title":"Netflix"}
    return render(request,'index.html',context)

def browseIndex(request):
    context = {"title": "Netflix - Browse"}
    return render(request,'browse-index.html',context)