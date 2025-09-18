from rest_framework.permissions import BasePermission

class IsAdmin(BasePermission):
    """
    Allows access admin.
    """

    def has_permission(self, request, view):
        # Complex checks
        return bool(request.user and request.user.is_authenticated and request.user.role == 'admin')


class IsVendor(BasePermission):
    """
    Allows access vendor.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'vendor')

class IsCustomer(BasePermission):
    """
    Allows access customer.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.role == 'customer')
