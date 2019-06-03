from django.db import models

class TB_Usuario(models.Model):
<<<<<<< Updated upstream
    id = models.AutoField(primary_key=True, name='id')
=======
    AVALIACOES = [
        ('Excelente', 'Excelente'),
        ('Bom', 'Bom'),
        ('Médio', 'Médio'),
        ('Ruim', 'Ruim'),
        ('Péssimo', 'Péssimo'),
    ]
    cpf = models.CharField(primary_key=True, max_length=11, name='cpf')
>>>>>>> Stashed changes
    email = models.EmailField(name='email')
    senha = models.CharField(max_length=20, name='senha')
    notificacao = models.BooleanField(name='notificacao')
    avaliacao = models.CharField(max_length=10, name='avaliacao', choices=AVALIACOES)
    comentarios = models.CharField(max_length=500, name='comentarios')
    class Meta:
        db_table = "TB_Usuarios"
