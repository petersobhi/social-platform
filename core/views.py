from django.db import IntegrityError
from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import viewsets, permissions, mixins, filters, decorators, parsers, response, status
from rest_framework.views import Response
from rest_framework.generics import ListAPIView

from core.models import Post, Comment, Like
from core.serializers import PostSerializer, PostAttachmentSerializer, CommentSerializer, LikeSerializer, UserSerializer
from core.permissions import IsOwner

User = get_user_model()


class PostViewSet(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @decorators.action(
        detail=True,
        methods=['PUT'],
        serializer_class=PostAttachmentSerializer,
        parser_classes=[parsers.MultiPartParser],
        permission_classes=(IsOwner,)
    )
    def attachment(self, request, pk):
        obj = self.get_object()
        serializer = self.serializer_class(obj, data=request.data,
                                           partial=True)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data)
        return response.Response(serializer.errors,
                                 status.HTTP_400_BAD_REQUEST)


class CommentViewSet(mixins.CreateModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Comment.objects.filter(post=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(user=self.request.user, post=post)


class LikeViewSet(mixins.CreateModelMixin,
                  viewsets.GenericViewSet):
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Like.objects.filter(post=self.kwargs['post_pk'])

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        try:
            serializer.save(user=self.request.user, post=post)
        except IntegrityError:  # TODO move this validation to serializer
            return Response("Only one like is allowed per post", status=400)


class UserListView(ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = User.objects.all()
