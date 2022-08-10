from django.urls import path

from .views import IndexView, index

urlpatterns = [
    path("", index),
    path("class/", IndexView.as_view()),
]
