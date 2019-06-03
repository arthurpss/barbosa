from django.db import models

class TB_Usuario(models.Model):
    #id = models.AutoField(primary_key=True, name='id')
    email = models.EmailField(name='email')
    senha = models.CharField(max_length=20, name='senha')
    notificacao = models.BooleanField(name='notificacao')
    avaliacao = models.CharField(max_length=5, name='avaliacao')
    comentarios = models.CharField(max_length=500, name='comentarios')

    class Meta:
        db_table = "TB_Usuarios"
