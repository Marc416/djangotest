from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        # hello_world_input이라는 이름을 가진 데이터를 가져와라
        input_data = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = input_data
        new_hello_world.save()

        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': 'It is Get'})
