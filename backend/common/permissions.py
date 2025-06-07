from rest_framework import permissions

class IsAdminOrReadOnly(permissions.BasePermission):
    """
    Only admin users can perform write operations.
    All users can read (GET, HEAD, OPTIONS).
    """
    def has_permission(self, request, view):
        # SAFE_METHODS = ['GET', 'HEAD', 'OPTIONS']
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated and request.user.is_staff
