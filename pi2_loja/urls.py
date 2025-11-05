from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

def redirecionar_para_login(request):
    return redirect('/contas/login/')

urlpatterns = [
    path('', redirecionar_para_login),  # ← redireciona para login
    path('admin/', admin.site.urls),
    path('produtos/', include('produtos.urls')),
    path('contas/', include('contas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

