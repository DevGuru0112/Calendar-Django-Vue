from django.db import models

# Create your models here.

class User(models.Model):
    class Meta():
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    

class Calendar(models.Model):
    class Meta():
        db_table = 'calendar'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    


class Date(models.Model):
    class Meta():
        db_table = 'date'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)


class Entry(models.Model):
    class Meta():
        db_table = 'entry'
    id = models.AutoField(primary_key=True)
    calendar_id = models.ForeignKey(to=Calendar, on_delete=models.CASCADE)
    user_id = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date_id = models.ForeignKey(to=Date, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)


class Resource(models.Model):
    class Meta():
        db_table = 'resource'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

class Event(models.Model):
    class Meta():
        db_table = 'event'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)