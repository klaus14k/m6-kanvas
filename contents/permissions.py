from rest_framework.permissions import BasePermission
from rest_framework import permissions

class CheckStudent(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user in obj.course.students.all()
            and request.method in permissions.SAFE_METHODS
            or request.user.is_superuser
        )

class isSuperUserOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_superuser)