from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_superuser', 'is_client', 'is_staff_member']
    list_filter = ['is_superuser', 'is_client', 'is_staff_member']
    
    fieldsets = UserAdmin.fieldsets + (
        (None, {
            'fields': (
                'is_client',
                'is_staff_member',
                'phone',
            )
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {
            'fields': (
                'is_client',
                'is_staff_member',
                'phone',
            )
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
