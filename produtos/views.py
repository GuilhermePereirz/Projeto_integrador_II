from django.shortcuts import render, redirect, get_object_or_404
from .models import Produto, Categoria, Subcategoria
from .forms import ProdutoForm, CategoriaForm,SubcategoriaForm
from django.views.decorators.http import require_POST
from django.core.paginator import Paginator

def adicionar_subcategoria(request):
    categoria_id = request.GET.get('categoria_id')
    initial_data = {}
    if categoria_id:
        initial_data['categoria'] = categoria_id

    form = SubcategoriaForm(request.POST or None, initial=initial_data)
    if form.is_valid():
        form.save()
        return redirect('gestao_categorias')
    return render(request, 'produtos/form_subcategoria.html', {'form': form})


def editar_subcategoria(request, id):
    sub = get_object_or_404(Subcategoria, id=id)
    form = SubcategoriaForm(request.POST or None, instance=sub)
    if form.is_valid():
        form.save()
        return redirect('gestao_categorias')
    return render(request, 'produtos/form_subcategoria.html', {'form': form})

@require_POST
def excluir_subcategoria(request, id):
    sub = get_object_or_404(Subcategoria, id=id)
    sub.delete()
    return redirect('gestao_categorias')

def lista_produtos(request):
    produtos = Produto.objects.filter(status='ativo')
    nome = request.GET.get('nome')
    categoria = request.GET.get('categoria')

    if nome:
        produtos = produtos.filter(nome__icontains=nome)
    if categoria:
        produtos = produtos.filter(categoria_id=categoria)

    paginator = Paginator(produtos, 9)  # 9 produtos por página
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categorias = Categoria.objects.all()

    return render(request, 'produtos/lista.html', {
        'produtos': page_obj,
        'categorias': categorias,
        'page_obj': page_obj
    })


def cadastrar_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('gestao_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/cadastrar.html', {'form': form})

def gestao_produtos(request):
    nome = request.GET.get('nome', '')
    categoria = request.GET.get('categoria', '')
    status = request.GET.get('status', '')

    produtos = Produto.objects.all()
    if nome:
        produtos = produtos.filter(nome__icontains=nome)
    if categoria:
        produtos = produtos.filter(categoria__icontains=categoria)
    if status:
        produtos = produtos.filter(status=status)

    return render(request, 'produtos/gestao.html', {'produtos': produtos})

def detalhes_produto(request, produto_id):
    produto = get_object_or_404(Produto, id=produto_id)
    return render(request, 'produtos/detalhes.html', {'produto': produto})

def editar_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, request.FILES, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('gestao_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/editar.html', {'form': form})

@require_POST
def excluir_produto(request, produto_id):
    produto = Produto.objects.get(id=produto_id)
    produto.delete()
    return redirect('gestao_produtos')


from .models import Categoria, Subcategoria

def gestao_categorias(request):
    categorias = Categoria.objects.all()
    subcategorias_por_categoria = {
        cat.id: Subcategoria.objects.filter(categoria=cat)
        for cat in categorias
    }
    return render(request, 'produtos/gestao_categorias.html', {
        'categorias': categorias,
        'subcategorias_por_categoria': subcategorias_por_categoria
    })


def adicionar_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('gestao_categorias')
    return render(request, 'produtos/form_categoria.html', {'form': form})

def editar_categoria(request, id):
    cat = Categoria.objects.get(id=id)
    form = CategoriaForm(request.POST or None, instance=cat)
    if form.is_valid():
        form.save()
        return redirect('gestao_categorias')
    return render(request, 'produtos/form_categoria.html', {'form': form})

@require_POST
def excluir_categoria(request, id):
    Categoria.objects.get(id=id).delete()
    return redirect('gestao_categorias')
