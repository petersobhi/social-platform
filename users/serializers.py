from django.contrib.auth import get_user_model
from rest_framework import serializers
from friendship.models import FriendshipRequest

from core.serializers import PostSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class UserProfileSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, source='post_set')

    class Meta:
        model = User
        fields = ['pk', 'username', 'email', 'posts']


class FriendshipRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = FriendshipRequest
        fields = ['id', 'from_user', 'to_user', 'message', 'created', 'rejected', 'viewed']