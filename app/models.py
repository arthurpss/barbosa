from django.db import models

class td_formulario(models.Model):
    pass

AVALIACOES = (
    ('Excelente', 10),
    ('Bom', 8),
    ('Médio', 5),
    ('Ruim', 3),
    ('Péssimo', 1)
)

class Usuario(models.Model):
    id = models.AutoField(primary_key=True, name='id')
    email = models.EmailField(name='email')
    senha = models.CharField(max_length=20, name='senha')
    notificacao = models.BooleanField(name='notificacao')
    avaliacao = models.CharField(max_length=5, choices=AVALIACOES, name='avaliacao')
    comentarios = models.CharField(max_length=500, name='comentarios')
    class Meta:
        db_table = "usuario"

    @classmethod
    def cria_id(classe, id):
        id = classe(id=id)
        return id

    @classmethod
    def cria_email(classe, email):
        email = classe(email=email)
        return email
    @classmethod
    def cria_senha(classe, senha):
        senha = classe(senha=senha)
        return senha

    @classmethod
    def cria_notificao(classe, notificao):
        notificao = classe(notificao)
        return notificao

    @classmethod
    def cria_avaliacao(classe, avaliacao):
        avaliacao = classe(avaliacao=avaliacao)
        return avaliacao

    @classmethod
    def cria_comentarios(classe, comentarios):
        comentarios = classe(comentarios=comentarios)
        return comentarios
