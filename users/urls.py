from django.urls import path, include

from rest_framework.routers import DefaultRouter

from .views import UserListView, UserProfileView, FriendViewSet, FriendshipRequestViewSet

router = DefaultRouter()
router.register(r'friends', FriendViewSet, basename='friends')
router.register(r'friends/requests', FriendshipRequestViewSet, basename='friendrequests')

urlpatterns = [
    path('users', UserListView.as_view()),
    path('users/<int:pk>', UserProfileView.as_view()),
    path('', include(router.urls)),
]
