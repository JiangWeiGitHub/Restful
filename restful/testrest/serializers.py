# coding=<utf-8>
from django.contrib.auth.models import User, Group
from models import addit 
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ADDITSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = addit
        fields = ('url','a','b','c')

class testadd(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = addit
        a=1
        fields = ('url','a','b','c',a)    

class CalcClass():
    def __init__(self):
        pass

    def do_work(self):
        result = ((1,2,3), (4,5,6))
        return result
