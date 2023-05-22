from django.contrib import admin
from django.urls import path, include
from. import views

from newapp.views import filtres_page

from django.urls import include, path
from rest_framework import routers
from .views import PharmaListApiView


urlpatterns = [
    path("", views.home),
    path('filtres/', filtres_page, name='filtres'),
    path('api/pharma/', PharmaListApiView.as_view()),
]