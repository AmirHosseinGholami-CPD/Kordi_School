from django.contrib.auth.mixins import AccessMixin
from django.shortcuts import redirect
from Admin.models import Admin_Web

class AdminRequiredMixin(AccessMixin):
    """Verify that the current user is an admin user."""
    def dispatch(self, request, *args, **kwargs):
        # Check if the user is in the Admin_Web table
        try:
            Admin_Web.objects.get(username=request.user.username)
        except Admin_Web.DoesNotExist:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
