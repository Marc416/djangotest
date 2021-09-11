from django.urls import include, path

import accountapp
from accountapp.views import hello_world, AccountCreateView

app_name = 'accountapp'

urlpatterns = [
    # 함수형 뷰를 이용할 때
    # 어떤 패스를 받으면(http어쩌고..hello_world/), hello_world 함수를 실행시키렴,
    # name = hello_world.html에 있는 것중에서!
    path('hello_world/', hello_world, name='hello_world'),
    # 클래스형 뷰를 이용할 때
    path('create/', AccountCreateView.as_view(), name='create'),
]
