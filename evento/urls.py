from django.urls import path
from .views import home

app_name = 'evento'
urlpatterns = [
    path('', home, name='home'),
]