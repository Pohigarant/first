from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    message = 'Вы не можеете редактировать данный обьект'

    def has_permission(self, request, view):
        return (request.user and request.user.is_authenticated) or request.method in permissions.SAFE_METHODS

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user


class IsBasketOwner(permissions.BasePermission):
    message = 'Вы не можеете смотреть данный обьект'
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user


class IsOwnerOrAdmin(permissions.BasePermission):
    message = "Вы не можете редактировать данный профиль"

    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_staff