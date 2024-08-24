from rest_framework import permissions
from rest_framework.generics import GenericAPIView
from rest_framework.views import Request

class IsSuperuser(permissions.BasePermission):
    def has_permission(self, request: Request, view: GenericAPIView):
        return (request.user.is_superuser or request.method in permissions.SAFE_METHODS)