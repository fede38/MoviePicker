from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/<int:movie_id>/', views.detail, name='movie'),
]
