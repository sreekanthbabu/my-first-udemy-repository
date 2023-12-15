from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog

# Create your views here.



def home(request):
    return HttpResponse("hello sreekanth this is home function and  for urls include usage")


def demo(request):
    return render(request,"demo.html",{"name":"Babu"})


def bhavani(request):
    return HttpResponse("Bhavani is looking at this very seriously")

def sree(request):
    data=Blog.objects.all()
    return render(request,"base.html",{"data":data})

