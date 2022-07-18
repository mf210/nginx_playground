from django.urls import path

from . import views


urlpatterns = [
    path('apitwo/', views.index)
]