from webbrowser import get
from django.db import models
from django.contrib.auth import get_user_model


class BlogPost(models.Model):
    title = models.CharField(max_length=65)
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
