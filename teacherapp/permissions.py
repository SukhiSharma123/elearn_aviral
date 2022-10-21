from rest_framework import permissions

class IsTeacherOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.user.is_superuser:
            return True
        # if request.method in "GET":
        #     return True

        # Instance must have an attribute named `user`.
        if obj.attended_by.user == request.user:
            return True
        if obj.created_by.user == request.user:
            return True

class IsMessageOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.user.is_superuser:
            return True
        # if request.method in "GET":
        #     return True

        # Instance must have an attribute named `user`.
        if obj.created_by.user == request.user:
            return True