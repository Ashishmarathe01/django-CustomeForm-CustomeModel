from django.contrib import admin
from .models import Newuser

from django.contrib.auth.admin import UserAdmin
# Register your models here.

class NewuserAdmin(UserAdmin):
    list_display = ('email','phone')
    search_fields = ('phone',)

    filter_horizontal = ()
    fieldsets = ()
    list_filter = ()





admin.site.register(Newuser,NewuserAdmin)
