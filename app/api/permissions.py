from rest_framework import permissions


class AdminOrReadOnly(permissions.IsAdminUser):
    """
    Custom permission to only allow admin users to edit objects.
    Non-admin users can only read objects.
    """

    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission
