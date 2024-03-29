from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    SAFE_METHODS,
    BasePermission,
)


class IsAuthorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS or request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return (request.method in SAFE_METHODS) or (obj.author == request.user)
