from rest_framework.permissions import BasePermission


class GradeManagerPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not request.user:
            return False
        if request.user.is_grade != 0:
            return True
        else:
            return False

class SuperManagerPermission(BasePermission):
    def has_permission(self, request, view):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        if not request.user:
            return False
        if request.user.is_super != 0:
            return True
        else:
            return False
