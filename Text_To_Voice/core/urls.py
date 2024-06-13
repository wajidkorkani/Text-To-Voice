from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('text-to-voice/', views.TextToVoice, name='text_to_voice'),
]
