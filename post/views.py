from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import generics
from .permissions import IsAuthorOrReadOnly


class BlogPostList(generics.ListCreateAPIView):
    queryset =  BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class BlogPostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
# Create your views here.
