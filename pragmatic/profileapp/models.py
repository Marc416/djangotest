from django.contrib.auth.models import User
from django.db import models


# Create your models here.

class Profile(models.Model):
    # 유저가 삭제될경우 유저 모델도 삭제하라
    # related_name ->이건 어딘가에서 플필을 불러왔을 때 바로 사용할 수 잇게 해주는 기능을 함.
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    # 미디어 루트 밑에 profile/해서 저장
    image = models.ImageField(upload_to='profile/', null=True, blank=True)
    nickname = models.CharField(max_length=20, unique=True, null=True, blank=True)
    message = models.CharField(max_length=100, null=True, blank=True)
