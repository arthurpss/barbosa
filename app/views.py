from django.shortcuts import render, redirect
from app.forms import UsuarioForm
from app.forms import TreinoForm
from app.models import TB_Usuario
from app.models import TB_Treino


def home(request):
    return render(request, 'app/home.html')


def create(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read')
        else:
            print('invalido')
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
    dados['usuario'] = usuario
    if request.method == 'POST':
        form = UsuarioForm(request.POST, instance=usuario)
        dados['form'] = form
        print(form.is_valid())
        if form.is_valid():
            print('valido')
            form.save()
            return redirect('/read')
    else:
        form = UsuarioForm()
        dados['form'] = form
    return render(request, 'app/update.html', dados)


def delete(request, cpf):
    usuario = TB_Usuario.objects.get(cpf=cpf)
    usuario.delete()
    return redirect('/read')

def create_treino(request):
    if request.method == "POST":
        form = TreinoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read_treino/')
    else:
        form = TreinoForm()
        return render(request, 'app/create_treino.html', {'form': form})

def read_treino(request):
    dados = {}
    dados['treinos'] = TB_Treino.objects.all()
    return render(request, 'app/read_treino.html', dados)