from django.contrib import admin
from django.urls import path, include
from. import views

from newapp.views import filtres_page


urlpatterns = [
    path("", views.home),
    path('filtres/', filtres_page, name='filtres')
]
