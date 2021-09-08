from django.urls import include, path

import accountapp
from accountapp.views import hello_world

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
]
