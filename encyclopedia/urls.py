from django.urls import path

from . import views

app_name = 'ency'
urlpatterns = [
    path("", views.index, name="index"),
    path("newpage", views.newpage, name='newpage'),
    path("randompage", views.random, name="randompage"),
    path("<str:title>", views.content, name="content")
]
