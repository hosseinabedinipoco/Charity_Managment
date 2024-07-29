from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DefaultUserAdmin
from .models import User
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active']
    list_filter = ['gender', 'is_staff', 'is_active', 'is_superuser']
    list_editable = ['is_staff', 'is_active']
    list_display_links = ['username']
    readonly_fields = ['password']
    fieldsets = (
        (None, {
            'fields' : ('username', 'password')
        }),
        ('Personal Info', {
            'fields' : ('first_name', 'last_name', 'email', 'gender', 'age', 'description')
        }), 
        ('contact info', {
            'fields' : ('phone', 'address')
        }), 
        ('Permission', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }), 
        ('important dates', {
            'fields' : ('last_login', 'date_joined')
        })
    )
