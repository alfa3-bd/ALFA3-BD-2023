from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("", include("apps.home.urls")),
    path("home/", include("apps.home.urls")),
    path("admin/", admin.site.urls),
    path("authentication/", include("apps.authentication.urls")),
    path("professor/", include("apps.professor.urls")),
    path("gestor/", include("apps.gestor.urls")),
]
