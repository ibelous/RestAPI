from rest_framework import permissions
from .models import Course, HomeWork


class TeacherPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.user_type == 2:
            return True
        return False


class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        user = request.user
        return Course.objects.filter(users=user)


class MyHomeWork(permissions.BasePermission):
    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False
        return HomeWork.objects.filter(student=request.user, ) or request.user.user_type == 2
