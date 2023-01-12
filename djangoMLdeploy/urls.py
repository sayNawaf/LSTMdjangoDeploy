
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("Home/", include('concepts.urls')),
    path("admin/", admin.site.urls),
]
