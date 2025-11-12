from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Cria grupos padrão e atribui permissões básicas'

    def handle(self, *args, **kwargs):
        grupos = ['Administrador', 'Funcionário', 'Cliente']
        for nome in grupos:
            group, created = Group.objects.get_or_create(name=nome)
            if created:
                self.stdout.write(self.style.SUCCESS(f'Grupo criado: {nome}'))
            else:
                self.stdout.write(self.style.WARNING(f'Grupo já existia: {nome}'))

        # Permissões exemplo (ajuste conforme seu app)
        admin = Group.objects.get(name='Administrador')
        funcionario = Group.objects.get(name='Funcionário')
        cliente = Group.objects.get(name='Cliente')

        # Admin: todas permissões de usuário
        perms = Permission.objects.filter(content_type__app_label='auth')
        admin.permissions.set(perms)

        # Funcionário: pode ver e alterar usuários (exemplo suave)
        view_change = Permission.objects.filter(
            content_type__app_label='auth',
            codename__in=['view_user', 'change_user']
        )
        funcionario.permissions.set(view_change)

        # Cliente: apenas visualizar a si mesmo (vamos deixar sem permissões globais)
        cliente.permissions.clear()

        self.stdout.write(self.style.SUCCESS('Permissões configuradas.'))
