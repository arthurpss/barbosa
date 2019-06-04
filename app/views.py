from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import TB_Usuario

def home(request):
    return render(request, 'app/home.html')

def formulario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/visualizar/')
        else:
            print(form.errors)
    else:
        form = UsuarioForm()
        return render(request, 'app/formulario.html', {'form': form})

def visualizador(request):
    dados = {}
    dados['usuarios'] = TB_Usuario.objects.all()
    return render(request, 'app/visualizar.html', dados)

def atualizar(request):
    return render(request, 'app/update.html')