from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from newsapp.models import Category, Authors, Articles
from newsapp.serializers import CategorySerializer, AuthorsSerializer, ArticlesSerializer



class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class AuthorsViewSet(viewsets.ModelViewSet):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer


class ArticlesViewSet(viewsets.ModelViewSet):
    queryset = Articles.objects.all()
    serializer_class = ArticlesSerializer

