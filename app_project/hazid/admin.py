from django.contrib import admin

from .models import Survey, AllowedUser, CustomUser

@admin.register(AllowedUser)
class AllowedUserAdmin(admin.ModelAdmin):
    list_display = ('email',)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email',)

admin.site.register(Survey)