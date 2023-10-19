
from django.contrib import admin
from django.urls import include , path

urlpatterns = [
    path('PytubeApp/',include('PytubeApp.urls')),

    path('admin/', admin.site.urls),
]
