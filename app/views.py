from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.models import TB_Usuario

def home(request):
    return render(request, 'app/home.html')

def create(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read/')
    else:
        form = UsuarioForm()
        return render(request, 'app/create.html', {'form': form})

def read(request):
    dados = {}
    dados['usuarios'] = TB_Usuario.objects.all()
    return render(request, 'app/read.html', dados)

def update(request, cpf):
    dados = {}
    usuario = TB_Usuario.objects.get(cpf=cpf)
    form = UsuarioForm(request.POST or None, instance=usuario)
    dados['usuario'] = usuario
    if form.is_valid():
        form.save()
        dados['form'] = form
        return redirect('/read/')
    return render(request, 'app/update.html', dados)

def delete(request, pk):
    return render(request, 'app/home.html')
