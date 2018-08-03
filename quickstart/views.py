from django.shortcuts import render
from django.contrib.auth.models import Group, User
from rest_framework import viewsets, generics
from quickstart.serializers import (
    UserSerializer, GroupSerializer, CeoSerializer,
    ProgrammerSerializer, ProjectSerializer, 
    LanguageSerializer
)
from .models import Ceo, Language, Programmer, Project


class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProgrammerViewSet(viewsets.ModelViewSet):

    queryset = Programmer.objects.all()
    serializer_class = ProgrammerSerializer


class LanguageViewSet(viewsets.ModelViewSet):
   
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer


class CeoViewSet(viewsets.ModelViewSet):
   
    queryset = Ceo.objects.all()
    serializer_class = CeoSerializer
