from django.contrib import admin
from django.contrib.auth.views import LogoutView, LoginView
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('candidato.urls', namespace='candidato')),
    path('', include('evento.urls', namespace='evento')),
    path('', include('usuarios.urls', namespace='usuarios')),
    path('', include('inscricao.urls', namespace='inscricao')),
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)