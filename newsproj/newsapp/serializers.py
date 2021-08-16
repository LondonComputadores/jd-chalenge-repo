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
    author = AuthorsSerializer(
        many=True,
        read_only=True,
    )

    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='title'
    )

    class Meta:
        model = Articles
        fields = ['id',
                  'author', 
                  'category',
                  'title',
                  'summary',
                  'firstParagraph']