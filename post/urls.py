from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, BlogPostViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users')
router.register('', BlogPostViewSet, basename='blog')


urlpatterns = router.urls