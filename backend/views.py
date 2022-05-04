from multiprocessing import Event
from django.shortcuts import render
import json

from backend.models import User, Resource, Entry, Date, Calendar, Event

from rest_framework import viewsets
from rest_framework import permissions

from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.http import JsonResponse
from backend.serializers import *

# Create your views here.


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


@api_view(['GET', 'POST'])
def user_list(request):
    """
    List all code users, or create a new snippet.
    """
    if request.method == 'GET':
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_infos(request):
    """
    List all code resources and events.
    """

    if request.method == 'GET':
        allresource = Resource.objects.all()
        resources = ResourceSerializer(allresource, many=True)
        allevents = Event.objects.all()
        events = EventSerializer(allevents, many=True)
        return Response({'resources': resources.data, 'events': events.data})


@api_view(['POST'])
def get_month_info(request):
    """
    List all code resources and events.
    """

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    currentmonth = body['currentmonth']
    print("curmonth", currentmonth)
    if request.method == 'POST':
        allresources = Resource.objects.all()
        resources = ResourceSerializer(allresources, many=True)
        
        allevents = Event.objects.all()
        events = EventSerializer(allevents, many=True)
        return Response({'resources': resources.data, 'events': events.data})


@api_view(['POST'])
def add_resource(request):
    " add on resource"
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    resourceName = body['resource']

    " find the resource with same name"
    obj = Resource.objects.filter(name=resourceName)
    resources = ResourceSerializer(obj, many=True)
    if resources == None:
        newResource = Resource()
        newResource.name = resourceName
        newResource.save()
        return Response({'success': True})
    else:
        return Response({'success': False})
