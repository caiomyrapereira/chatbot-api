# from django.shortcuts import render

# Create your views here.

# from django.shortcuts import render
from rest_framework.decorators import api_view
from .business import  Init, chat
from .serializer import  StartChatSerializer, DataSerializer
from django.http.response import JsonResponse
from rest_framework.response import Response

# Create your views here.

@api_view(['GET'])
def start(request):
 init = Init.init()
 init_serializer = StartChatSerializer(init)
 return JsonResponse(init_serializer.data, safe=False)


@api_view(['POST'])
def postData(request):
 print("data do caio:")
 data = DataSerializer(data=request.data)
 print(data)
 if data.is_valid():
  print(data.data["description"])
  newData = DataSerializer(chat.chat(data.data["description"]))
  print(newData)
  setattr(data, 'description', "default...")

  return JsonResponse(newData.data, safe=False)
  print("erro do caio")