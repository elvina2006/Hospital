from rest_framework.permissions import BasePermission
from rest_framework import permissions


class CheckDoctor(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'врач':
            return True

