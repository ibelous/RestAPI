from rest_framework import permissions


class TeacherPermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        if user.is_authenticated and user.user_type == 2:
            return True
        return False
