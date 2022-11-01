from rest_framework.permissions import BasePermission

class AdminCheckPermission(BasePermission):
    def has_permission(self, request, view):
        edit_methods = ("PUT", "PATCH","POST","DELETE")
        if request.method in edit_methods:
            if  request.user.is_superuser:

                return True
            return False
       
       
       

class DeveloperAdminCheckPermission(BasePermission):
    def has_permission(self, request, view):
        if not (request.user.is_superuser and request.user.user_role == "developer"):
            return False

       

        