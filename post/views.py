from .models import BlogPost
from rest_framework import viewsets
from .serializers import BlogPostSerializer, UserSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly

from django.contrib.auth import get_user_model


class BlogPostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer


# Create your views here.
