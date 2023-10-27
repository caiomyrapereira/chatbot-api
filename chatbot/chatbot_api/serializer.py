from rest_framework import serializers
from .models import Pergunta, Resposta, StartChat, Data
class RespostaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resposta
        fields = '__all__'
class PerguntaSerializer(serializers.ModelSerializer):
    respostas = RespostaSerializer(many=True)
    class Meta:
        model = Pergunta
        fields = '__all__'

class StartChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = StartChat
        fields = '__all__'


# class ChatSerializer(serializers.ModelSerializer):
  #  class Meta:
   #     model = Chat
   #     fields = '__all__'


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        fields=('name', 'description')