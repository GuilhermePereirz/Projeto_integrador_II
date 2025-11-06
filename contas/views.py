# contas/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def painel_admin(request):
    return render(request, 'painel_admin.html')

def home(request):
    return render(request, 'home.html')

def sobre(request):
    return render(request, 'sobre.html')

def contato(request):
    return render(request, 'contato.html')

def portfolio(request):
    return render(request, 'portfolio.html')


