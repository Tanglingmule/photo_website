#app level urls (photo_repo)
from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name='home'),
    path('gallery', views.gallery_one, name='gallery'),
    path('gallerytwo', views.gallery_two, name='gallerytwo'),
}