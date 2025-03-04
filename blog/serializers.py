from rest_framework import serializers
from .models import Category
from .models import Publication

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class PublicationSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Publication
        fields = ['id', 'title', 'content', 'author', 'created_at']