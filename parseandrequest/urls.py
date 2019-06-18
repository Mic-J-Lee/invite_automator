from django.urls import path

from . import views

urlpatterns = [
    path('zapierpayload', views.zapiertogithub, name='zapiertogithub'),
]