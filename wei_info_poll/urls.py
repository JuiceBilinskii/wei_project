from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('characters/', views.characters)
]