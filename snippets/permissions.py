from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custo permission to only allow owners of an object to edit it
    """
    
    def has_object_permission(self, request, view, obj):
        # Read permissions are allower to any request
        # so we`ll always allow GET, HEAD or OPTIONS request
        if request.method in permissions.SAFE_METHODS:
            return True
        
        # Write permissions are only allower to the owner of the snippet
        return obj.owner == request.user