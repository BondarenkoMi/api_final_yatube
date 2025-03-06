from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, CommentViewSet, FollowViewSet, GroupViewSet

app_name = 'api'

router = SimpleRouter()
router.register(r'posts', PostViewSet)
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'groups', GroupViewSet)
router.register(r'follow', FollowViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls.jwt'))
]
