from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="homepage"),
    path('', views.maintenance, name='maintenance'),
]