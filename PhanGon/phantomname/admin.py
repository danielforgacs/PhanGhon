from django.contrib import admin
from . import models



@admin.register(models.User)
class User(admin.ModelAdmin):
    list_display = (
        'username',
        'is_staff',
        'is_superuser',
    )




@admin.register(models.GhostName)
class GhostName(admin.ModelAdmin):
    list_display = (
        'name',
        'description',
    )




@admin.register(models.PhantomName)
class PhantomName(admin.ModelAdmin):
    list_display = (
        'user',
        'ghostname',
    )
