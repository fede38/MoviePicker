from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('movie/<int:movie_id>/', views.detail, name='detail'),
]