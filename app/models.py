from django.db import models

class TB_Autor(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, name='cpf', unique=True)
    nome = models.CharField(max_length=60, name='nome')
    nacionalidade = models.CharField(max_length=40, name='nacionalidade')
    class Meta:
        db_table = "TB_Autor"


class TB_Livro(models.Model):
    isbn = models.IntegerField(primary_key=True, name='isbn', unique=True)
    nome = models.CharField(max_length=80, name='nome')
    editora = models.CharField(max_length=100, name='editora')
    autor = models.ForeignKey(TB_Autor, on_delete=models.CASCADE, name='autor')
    descricao = models.TextField(max_length=500, name='descricao')
    class Meta:
        db_table = "TB_Livro"
