from django.urls import path
from .views import *
urlpatterns = [
    path('notices/', notice_list, name='notice_list'),
]
