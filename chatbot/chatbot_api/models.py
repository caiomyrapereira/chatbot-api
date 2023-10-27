from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class Resposta(models.Model):
   codigo = models.IntegerField()
   valor = models.CharField(max_length=1)
   descricao = models.TextField(blank=False, null=False)
   acao = models.TextField(blank=False, null=False)


class Pergunta(models.Model):
    codigo = models.IntegerField()
    titulo = models.TextField(blank=False, null=False)
    respostas = models.ManyToManyField(Resposta)


class StartChat(models.Model):
    chat = models.TextField(blank=False, null=False)

# Create your models here.
class Data(models.Model):
    name = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

## class Chat(models.Model):
   ## usuarioPergunta = models.TextField(blank=False, null=False)
    ## chatbotResposta = models.TextField(blank=False, null=False)
