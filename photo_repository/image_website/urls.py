#app level urls (photo_repo)
from django.urls import path
from . import views

urlpatterns = {
    path('', views.home, name='home'),
}