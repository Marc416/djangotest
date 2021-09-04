from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def hello_world(request):
    #어떻게 여기서 새로 만든 accountapp 폴더를 추적해서 hello_world.html을 찾는가?
    return render(request,'accountapp/hello_world.html')