from __future__ import print_function, unicode_literals

from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets, decorators, permissions
from rest_framework.response import Response
from friendship.models import Friend, FriendshipRequest

from .serializers import UserSerializer, FriendshipRequestSerializer


class FriendViewSet(viewsets.ViewSet):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def list(self, request):
        friends = Friend.objects.friends(request.user)
        serializer = self.serializer_class(friends, many=True)
        return Response(serializer.data)

    @decorators.action(detail=False)
    def requests(self, request):
        friend_requests = Friend.objects.unrejected_requests(user=request.user)
        return Response(FriendshipRequestSerializer(friend_requests, many=True).data)

    def create(self, request):
        """
        Creates a friend request
        """
        friend_obj = Friend.objects.add_friend(
            request.user,  # The sender
            get_object_or_404(get_user_model(), pk=request.data['user_id']),  # The recipient
            message=request.data.get('message', '')
        )

        return Response(
            FriendshipRequestSerializer(friend_obj).data,
            status.HTTP_201_CREATED
        )


class FriendshipRequestViewSet(viewsets.ViewSet):
    """
    ViewSet for FriendshipRequest model
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = FriendshipRequestSerializer

    @decorators.action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk, to_user=request.user)
        friendship_request.accept()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )

    @decorators.action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        friendship_request = get_object_or_404(FriendshipRequest, pk=pk, to_user=request.user)
        friendship_request.reject()
        return Response(
            FriendshipRequestSerializer(friendship_request).data,
            status.HTTP_201_CREATED
        )
