# produtos/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar/', views.cadastrar_produto, name='cadastrar_produto'),
    path('gestao/', views.gestao_produtos, name='gestao_produtos'),
    path('', views.lista_produtos, name='lista_produtos'),
    path('<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('editar/<int:produto_id>/', views.editar_produto, name='editar_produto'),
    path('excluir/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
    path('categorias/', views.gestao_categorias, name='gestao_categorias'),
    path('categorias/adicionar/', views.adicionar_categoria, name='adicionar_categoria'),
    path('categorias/editar/<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('categorias/excluir/<int:id>/', views.excluir_categoria, name='excluir_categoria'),
    path('subcategorias/adicionar/', views.adicionar_subcategoria, name='adicionar_subcategoria'),
    path('subcategorias/editar/<int:id>/', views.editar_subcategoria, name='editar_subcategoria'),
    path('subcategorias/excluir/<int:id>/', views.excluir_subcategoria, name='excluir_subcategoria'),
]

