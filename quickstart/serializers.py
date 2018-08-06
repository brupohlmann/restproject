from django.contrib.auth.models import User, Group
from rest_framework import serializers

from .models import Ceo, Language, Programmer, Project


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Programmer
        fields = ('id','name', 'project')


class LanguageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Language
        fields = ('id','name')


class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('id','name','language', 'ceo')


class CeoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Ceo
        fields = ('id','name')
              
