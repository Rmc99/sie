from django.urls import path
from .views import efetuar_inscricao

app_name = 'inscricao'
urlpatterns = [
    path('efetuar_inscricao/', efetuar_inscricao, name='efetuar_inscricao'),
]
