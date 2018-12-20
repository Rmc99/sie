from django.urls import path
from .views import cadastro_candidato, dashboard, atualiza_candidato

app_name = 'candidato'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro_candidato/', cadastro_candidato, name='cadastro_candidato'),
    path('atualiza_candidato/<int:pk>', atualiza_candidato, name='atualiza_candidato'),
]