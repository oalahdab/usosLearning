"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from usosLearning import models

class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'FirstName', 'is_superuser']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': ('FirstName',)}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_staff',
                    'is_superuser',
                )
            }
        ), 
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Course)