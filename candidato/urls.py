from django.urls import path
from .views import cadastro_candidato, dashboard

app_name = 'candidato'
urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('cadastro_candidato/', cadastro_candidato, name='cadastro_candidato'),
]
