from rest_framework import serializers

from core.models import Post, Comment, Like

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user']