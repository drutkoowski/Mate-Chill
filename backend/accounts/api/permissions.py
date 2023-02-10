from rest_framework.permissions import BasePermission


class IsAuthenticated(BasePermission):
    """
    Allows access only to non authenticated users.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated()