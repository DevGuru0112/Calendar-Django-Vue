from backend.models import *
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name']

class CalendarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Calendar
        fields = ['id', 'name']


class DateSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Date
        fields = ['id', 'name']

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        calendar_id = CalendarSerializer(many=True, required=True)
        user_id = UserSerializer(many=True, required=True)
        date_id = DateSerializer(many=True, required=True)
        fields = ['id', 'name','calendar_id','user_id','date_id']

class ResourceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Resource
        fields = ['id', 'name']

class EventSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Event
        fields = ['id', 'name']