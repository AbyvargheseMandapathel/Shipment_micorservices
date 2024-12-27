# user/permissions.py

from rest_framework import permissions

class IsFirstCategory(permissions.BasePermission):
    """
    Custom permission to allow only users with 'is_first_category' set to True.
    """
    def has_permission(self, request, view):
        return request.user.is_first_category


class IsSecondCategory(permissions.BasePermission):
    """
    Custom permission to allow only users with 'is_second_category' set to True.
    """
    def has_permission(self, request, view):
        return request.user.is_second_category


class IsThirdCategory(permissions.BasePermission):
    """
    Custom permission to allow only users with 'is_third_category' set to True.
    """
    def has_permission(self, request, view):
        return request.user.is_third_category


class IsFourthCategory(permissions.BasePermission):
    """
    Custom permission to allow only users with 'is_fourth_category' set to True.
    """
    def has_permission(self, request, view):
        return request.user.is_fourth_category
