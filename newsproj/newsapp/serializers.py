from rest_framework import serializers
from newsapp.models import Category, Authors, Articles


class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"


class AuthorsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Authors
        fields = "__all__"


class ArticlesSerializer(serializers.ModelSerializer):
   """Allow to choose only the fields that will be visible on API"""
   class Meta:
        model = Articles
        fields = ['author', 
                  'category',
                  'title',
                  'summary',
                  'firstParagraph']