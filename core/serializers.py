from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers

from core.models import Post, Comment, Like

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', 'likes_count', 'attachment']


class PostAttachmentSerializer(serializers.ModelSerializer):  # To handle the attachment upload using multipart
    class Meta:
        model = Post
        fields = ['attachment']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', 'post']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user', 'post']
