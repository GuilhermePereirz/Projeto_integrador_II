from django.urls import path
from . import views

urlpatterns = [
    path('usuarios/', views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/cadastrar/', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/<int:user_id>/editar/', views.editar_usuario, name='editar_usuario'),
    path('usuarios/<int:user_id>/excluir/', views.excluir_usuario, name='excluir_usuario'),
    path("contato/", views.contato, name="contato"),
    path("mensagens/", views.listar_mensagens, name="listar_mensagens"),
]