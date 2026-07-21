from django.contrib import admin
from users.models import CustomUser

class Useradmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, Useradmin)