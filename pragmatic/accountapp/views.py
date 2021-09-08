from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def hello_world(request):
    if request.method == "POST":
        # hello_world_input이라는 이름을 가진 데이터를 가져와라
        temp = request.POST.get('hello_world_input')
        return render(request, 'accountapp/hello_world.html', context={'text': temp})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'It is Get'})
