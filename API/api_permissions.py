from rest_framework import permissions
from .models import Course, HomeWork, RateComment, WorkRate


class TeacherPermissionsOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if request.method in permissions.SAFE_METHODS:
            return True
        if user.is_authenticated and user.user_type == 2:
            return True
        return False


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
        if view.kwargs.get('course_id'):
            course_id = view.kwargs['course_id']
            return Course.objects.filter(users=user, id=course_id)
        elif view.kwargs.get('pk'):
            course_id = view.kwargs['pk']
            return Course.objects.filter(users=user, id=course_id)
        return False


class MyHomeWork(permissions.BasePermission):
    def has_permission(self, request, view):
        if view.kwargs.get('homework_id'):
            return HomeWork.objects.filter(student=request.user, id=view.kwargs['homework_id']) \
                   or request.user.user_type == 2
        return False
