from django.shortcuts import render
from app.forms import UsuarioForm

def home(request):
    return render(request, 'app/home.html')

def formulario(request):
    return render(request, 'app/formulario.html')

def visualizador(request):
    form = UsuarioForm(request.POST)
    if form.is_valid():
        form.save()
    else:
        print('caiu no else')
        form = UsuarioForm()
    return render(request, 'app/visualizar.html', {'form': form})
