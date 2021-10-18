from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from . import models
from . import serializers
from rest_framework.decorators import api_view


@api_view(['GET'])
def userList(request):
    users = models.User.objects.all()
    dataSerializers = serializers.UserSerializer(users, many=True)
    return Response(dataSerializers.data)


@api_view(['POST'])
def userDetail(request):

    if 'userid' in request.POST.keys() and request.POST['userid']:
        userId = request.data['userid']
    else:
        return Response({"message": "userid cannot be empty"})
    
    users = models.User.objects.get(userid= userId)
    dataSerializers = serializers.UserSerializer(users)

    if dataSerializers.data:
        return Response(dataSerializers.data)
    else:
        return Response({"message": "data not found"})
