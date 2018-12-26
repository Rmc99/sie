from django.urls import path
from .views import efetuar_inscricao, comprovante_inscricao

app_name = 'inscricao'
urlpatterns = [
    path('efetuar_inscricao/', efetuar_inscricao, name='efetuar_inscricao'),
    path('comprovante_inscricao/<int:pk>', comprovante_inscricao, name='comprovante_inscricao'),
]
