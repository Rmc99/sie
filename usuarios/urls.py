from django.urls import path
from .views import registrar

app_name = 'usuarios'
urlpatterns = [
    path('registrar/', registrar, name='registrar'),
]