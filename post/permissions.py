from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        #allow read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        #allow write permissions from author of a post
        return obj.author == request.user