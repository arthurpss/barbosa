from django.db import models

class TB_Treino(models.Model):
    nome = models.CharField(primary_key=True, max_length=20, name='nome')
    tipo = models.CharField(max_length=20, name='tipo')

    class Meta:
        db_table = "TB_Treino"

class TB_Usuario(models.Model):

    cpf = models.IntegerField(primary_key=True, name='cpf')
    email = models.EmailField(name='email')
    senha = models.CharField(max_length=20, name='senha')
    treino = models.ForeignKey(TB_Treino, on_delete=models.CASCADE)

    class Meta:
        db_table = "TB_Usuario"