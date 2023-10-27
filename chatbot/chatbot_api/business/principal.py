from ..models import Pergunta, Resposta
def obterMenuPrincipal():
 pergunta = Pergunta()
 pergunta.codigo = 1
 pergunta.titulo = "Selecione a opção desejada"

 resposta1 = Resposta()
 resposta1.codigo = 1
 resposta1.valor = '1'
 resposta1.descricao = "Saldo pontos fidelidade"
 resposta1.acao = "saldo-pontos"

 resposta2 = Resposta()
 resposta2.codigo = 2
 resposta2.valor = '2'
 resposta2.descricao = "Faturas em aberto"
 resposta2.acao = "aturas-aberto"
 resposta3 = Resposta()
 resposta3.codigo = 3
 resposta3.valor = '3'
 resposta3.descricao = "Comunicar perda de cartão"
 resposta3.acao = "perda-cartao"
 pergunta.save()
 resposta1.save()
 resposta2.save()
 resposta3.save()
 pergunta.respostas.add(resposta1)
 pergunta.respostas.add(resposta2)
 pergunta.respostas.add(resposta3)
 return pergunta