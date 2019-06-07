from django.shortcuts import render, redirect
from app.forms import AutorForm, LivroForm
from app.models import TB_Autor, TB_Livro


def home(request):
    return render(request, 'app/home.html')


def create_livro(request):
    if request.method == "POST":
        form = LivroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read-livro/')
    else:
        form = LivroForm()
        return render(request, 'app/create-livro.html', {'form': form})


def read_livro(request):
    livros = TB_Livro.objects.all()
    return render(request, 'app/read-livro.html', {'livros': livros})


def update_livro(request, isbn):
    dados = {}
    livro = TB_Livro.objects.get(isbn=isbn)
    form = LivroForm(request.POST or None, instance=isbn)
    dados['livro'] = livro
    if form.is_valid():
        form.save()
        dados['form'] = form
        return redirect('/read-livro/')
    return render(request, 'app/update-livro.html', dados)


def delete_livro(request, isbn):
    livro = TB_Livro.objects.get(isbn=isbn)
    livro.delete()
    return redirect('/read-livro/')


def create_autor(request):
    if request.method == "POST":
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read-autor/')
    else:
        form = AutorForm()
        return render(request, 'app/create-autor.html', {'form': form})


def read_autor(request):
    autores = TB_Autor.objects.all()
    return render(request, 'app/read-autor.html', {'autores': autores})


def update_autor(request, cpf):
    dados = {}
    autor = TB_Autor.objects.get(cpf=cpf)
    form = AutorForm(request.POST or None, instance=cpf)
    dados['autor'] = autor
    if form.is_valid():
        form.save()
        dados['form'] = form
        return redirect('/read-autor/')
    return render(request, 'app/update-autor.html', dados)


def delete_autor(request, cpf):
    autor = TB_Autor.objects.get(cpf=cpf)
    autor.delete()
    return redirect('/read-autor/')
