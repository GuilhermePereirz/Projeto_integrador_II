from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect
from contas import views as contas_views   # <-- este import estava faltando
from produtos import views as produtos_views
from usuarios import views

def redirecionar_para_login(request):
    return redirect('/contas/login/')

urlpatterns = [
    path('', redirecionar_para_login),  # ← redireciona para login
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('contas/', include('contas.urls')),
    path('sobre/', contas_views.sobre, name='sobre'),
    path('contato/', contas_views.contato, name='contato'),
    path('portfolio/', contas_views.portfolio, name='portfolio'),
    path('produtos/', produtos_views.lista_produtos, name='lista'),
    path('', include('usuarios.urls')),
    path("mensagens/", views.listar_mensagens, name="listar_mensagens"),
    path("contato/", views.contato, name="contato"),
     path("contato/", include("usuarios.urls")),  # ou direto se for simples
    path("mensagens/", include("usuarios.urls")),
 ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

