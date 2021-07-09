from django.urls import path, include

from rest_framework_nested import routers

from core import views

router = routers.SimpleRouter()
router.register(r'posts', views.PostViewSet)

posts_router = routers.NestedSimpleRouter(router, r'posts', lookup='post')
posts_router.register(r'comments', views.CommentViewSet, basename='post-comments')
posts_router.register(r'likes', views.LikeViewSet, basename='post-likes')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]