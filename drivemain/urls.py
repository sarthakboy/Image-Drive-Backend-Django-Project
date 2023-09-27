from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("",views.my_view,name = "my-view"),
    path("home/",views.homepage,name = "home-page"),
] +  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)