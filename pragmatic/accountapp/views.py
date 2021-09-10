from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from accountapp.models import HelloWorld


def hello_world(request):
    if request.method == "POST":
        # hello_world_input이라는 이름을 가진 데이터를 가져와라
        input_data = request.POST.get('hello_world_input')

        # DB인스턴스 생성
        new_hello_world = HelloWorld()
        # Add data
        new_hello_world.text = input_data
        # DB 저장
        new_hello_world.save()

        # SQL SELECT ALL
        hello_world_list = HelloWorld.objects.all()

        # 재연결시(새로고침) Get으로 해당 페이지 보여줄 수 있도록
        # 솔직히 reverse가 뭐 하는 건지모르겠음.
        # 왜 String으로 변수들을 불러서 쓰는지도 모르겠음->이거 엄청 불편하지 않나?
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        # 렌더가 무슨 역할을 하는지 궁금하다.
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
