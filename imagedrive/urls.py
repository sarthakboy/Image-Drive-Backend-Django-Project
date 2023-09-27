from django.contrib import admin
from django.urls import path, include
from drivemain import urls as drivemain_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include(drivemain_urls)),
]
