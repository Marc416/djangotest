from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from accountapp.decorator import account_ownership_required
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld

has_ownership = [account_ownership_required, login_required]


def modal_test(request):
    if request.method == "POST":
        # hello_world_input이라는 이름을 가진 데이터를 가져와라
        input_data = request.POST.get('modal_test')

        # DB인스턴스 생성
        new_hello_world = HelloWorld()
        # Add data
        new_hello_world.text = input_data
        # DB 저장
        new_hello_world.save()

        # 재연결시(새로고침) Get으로 해당 페이지 보여줄 수 있도록
        # 솔직히 reverse가 뭐 하는 건지모르겠음.
        # 왜 String으로 변수들을 불러서 쓰는지도 모르겠음->이거 엄청 불편하지 않나?
        return HttpResponseRedirect(reverse('modal.html'))
    else:
        hello_world_list = HelloWorld.objects.all()
        # 렌더가 무슨 역할을 하는지 궁금하다.
        # return HttpResponseRedirect(reverse('modal.html'))
        return render(request, 'modal.html')


@login_required
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

        # 재연결시(새로고침) Get으로 해당 페이지 보여줄 수 있도록
        # 솔직히 reverse가 뭐 하는 건지모르겠음.
        # 왜 String으로 변수들을 불러서 쓰는지도 모르겠음->이거 엄청 불편하지 않나?
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        # 렌더가 무슨 역할을 하는지 궁금하다.
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})


class AccountCreateView(CreateView):
    # 어떤 모델을 쓸 것인가?
    model = User
    # 장고에서 제공해주는 가입 폼을 사용
    form_class = UserCreationForm
    # 계정만들기에 성공시 어디로 가게 할 것인가
    # reverse_lazy는 클래스형 뷰 호출, reverse는 함수형 뷰 호출이라고만 알면 됨.
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'


class AccountDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'accountapp/detail.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:
            return super().get(*args, **kwargs)
        else:
            return HttpResponseForbidden()


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):
    model = User
    context_object_name = 'target_user'
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/update.html'


@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    # success_url이라는게 다음 실행되는게 성공하면인가?
    template_name = 'accountapp/delete.html'

# 아래 코드와 account_ownership_required와 같다는데 잘모르겠다.
# def get(self, *args, **kwargs):
#     if self.request.user.is_authenticated and self.get_object() == self.request.user:
#         return super().get(*args, **kwargs)
#     else:
#         return HttpResponseForbidden()
#
# def post(self, *args, **kwargs):
#     if self.request.user.is_authenticated and self.get_object() == self.request.user:
#         return super().post(*args, **kwargs)
#     else:
#         return HttpResponseForbidden()
