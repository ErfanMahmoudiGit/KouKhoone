from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUser(BasePermission):
    def has_permission (self, request, view):
        return bool(request.user and request.user.is_superuser)

class IsStaffOrReadOnly(BasePermission):
    def has_permission (self, request, view):
        return bool(
        request.method in SAFE_METHODES or
        request.user and request.user.is_staff
        )
