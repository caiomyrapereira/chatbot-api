from rest_framework import serializers
from .models import  StartChat, Data
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