from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Survey, AllowedUser, CustomUser

@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    list_display = ('email',)

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active', 'groups',)  # Добавьте 'groups' в список фильтров


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Survey)