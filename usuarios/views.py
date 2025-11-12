from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, Group
from .forms import UsuarioCreateForm, UsuarioUpdateForm

@login_required
@permission_required('auth.view_user', raise_exception=True)
def listar_usuarios(request):
    usuarios = User.objects.all().order_by('username')
    return render(request, 'usuarios/listar.html', {'usuarios': usuarios})

@login_required
@permission_required('auth.add_user', raise_exception=True)
def cadastrar_usuario(request):
    if request.method == 'POST':
        form = UsuarioCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioCreateForm()
    return render(request, 'usuarios/cadastrar.html', {'form': form})

@login_required
@permission_required('auth.change_user', raise_exception=True)
def editar_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)

    initial = {}
    first_group = usuario.groups.first()
    if first_group:
        initial['grupo'] = first_group.id

    if request.method == 'POST':
        form = UsuarioUpdateForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            return redirect('listar_usuarios')
    else:
        form = UsuarioUpdateForm(instance=usuario, initial=initial)

    return render(request, 'usuarios/editar.html', {'form': form, 'usuario': usuario})

@login_required
@permission_required('auth.delete_user', raise_exception=True)
def excluir_usuario(request, user_id):
    usuario = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        usuario.delete()
        return redirect('listar_usuarios')
    return render(request, 'usuarios/excluir.html', {'usuario': usuario})
