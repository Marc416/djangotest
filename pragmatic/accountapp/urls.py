from django.contrib.auth.views import LoginView, LogoutView
from django.urls import include, path

import accountapp
from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView, \
    modal_test

app_name = 'accountapp'

urlpatterns = [
    # 함수형 뷰를 이용할 때
    # 어떤 패스를 받으면(http어쩌고..hello_world/), hello_world 함수를 실행시키렴,
    # name = hello_world.html에 있는 것중에서!
    path('hello_world/', hello_world, name='hello_world'),
    path('modal/', modal_test, name='modal_test'),
    # 클래스형 뷰를 이용할 때
    path('create/', AccountCreateView.as_view(), name='create'),

    # 장고 기본 제공하는 로그인, 로그아웃 뷰 ; 장고로그인 폼뷰를 쓰려면 템플릿을 연결해야 함
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # Detail View
    # pk를 받겠다 근데 이 pk 는 int 이다
    # as_view()는 Class Based View에서 뷰를 호출할 때 쓴다.
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]
