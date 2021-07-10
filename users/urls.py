from rest_framework.routers import DefaultRouter

from .views import FriendViewSet, FriendshipRequestViewSet

router = DefaultRouter()
router.register(r'friends', FriendViewSet, basename='friends')
router.register(r'friends/requests', FriendshipRequestViewSet, basename='friendrequests')
urlpatterns = router.urls