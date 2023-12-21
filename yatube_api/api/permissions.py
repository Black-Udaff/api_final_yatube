from rest_framework.permissions import IsAuthenticatedOrReadOnly, SAFE_METHODS


class IsAuthorPermission(IsAuthenticatedOrReadOnly):

    def has_object_permission(self, request, view, obj):
        is_authenticated = super().has_permission(request, view)
        if request.method not in SAFE_METHODS:
            return is_authenticated and (obj.author == request.user)
        return is_authenticated
