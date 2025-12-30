from rest_framework import permissions


class UserStatusPermission(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.status == 'pro':
            return True
        elif request.user.status == 'simple' and obj.movie_atatus == 'simple':
            return True
        return False

class CreatePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.status == 'pro':
            return True
        else:
            return False