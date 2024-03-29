from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin

# Register your models here.

@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom user Admin"""

    list_display = ('username','first_name', 'last_name','email', 'is_active','language','currency','superhost','is_staff', 'is_superuser')
    list_filter = UserAdmin.list_filter + ('superhost',)

    fieldsets = UserAdmin.fieldsets + (
        ('Custom Profile',{'fields': ('avatar', 'gender', 'bio','birthdate', 'language', 'currency', 'superhost')}),
    )
