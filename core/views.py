from django.db import IntegrityError
from rest_framework import viewsets, permissions
from rest_framework.views import Response

from core.models import Post, Comment, Like
from core.serializers import PostSerializer, CommentSerializer, LikeSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(user=self.request.user, post=post)


class LikeViewSet(viewsets.ModelViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(post=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        try:
            serializer.save(user=self.request.user, post=post)
        except IntegrityError: # TODO move this validation to serializer
            return Response("Only one like is allowed per post", status=400)