from django.shortcuts import render
from app.forms import UsuarioForm

def home(request):
    return render(request, 'app/home.html')

def formulario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'app/visualizar.html')
        else:
            return render(request, 'app/formulario.html', {'form': form})
    else:
        form = UsuarioForm()
        return render(request, 'app/formulario.html', {'form': form})

def visualizador(request):
    return render(request, 'app/visualizar.html')
