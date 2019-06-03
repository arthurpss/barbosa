from django.shortcuts import render
from app.forms import UsuarioForm

def home(request):
    return render(request, 'app/home.html')

def formulario(request):
    form = UsuarioForm(request.POST)
    return render(request, 'app/formulario.html', {'form': form})

def visualizador(request):
    return render(request, 'app/visualizar.html')

def update(request):
    return render(request, 'app/update.html')