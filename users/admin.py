from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'is_staff']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'room')}),
        ('Personal Info', {'fields': ('first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
