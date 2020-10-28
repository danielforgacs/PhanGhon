from django.contrib import admin
from . import models



@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = (
        'username',
        'is_staff',
        'is_superuser',
    )
