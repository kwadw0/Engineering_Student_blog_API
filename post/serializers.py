from rest_framework import serializers
from .models import BlogPost

#this serializer class is used toi transform our models into JSON
class BlogPostSerializer(serializers.ModelSerializer):

    class Meta:
        model = BlogPost
        fields = ('id', 'title', 'body', 'author', 'created_at')