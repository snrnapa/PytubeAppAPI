from django.urls import path

from . import views

urlpatterns = [
    path('', views.youtube_download, name="youtube_download"),
]