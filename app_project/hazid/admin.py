from django.contrib import admin

from .models import Survey

# Register your models here.

class SurveyAdmin(admin.ModelAdmin):
    list_display = ["title", "created_at", "name", "age", "jeans"]
    list_filter = ["jeans"]

admin.site.register(Survey, SurveyAdmin)