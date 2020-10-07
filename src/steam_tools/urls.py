from django.urls import path
from . import views

urlpatterns = [
    path('swf', views.steam_with_friends, name='steam_with_friends')
]
