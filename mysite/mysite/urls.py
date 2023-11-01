from django.contrib import admin
from django.urls import include, path
from django.urls import path


urlpatterns = [
    path("", include("polls.urls")),
    path("admin/", admin.site.urls),
]
