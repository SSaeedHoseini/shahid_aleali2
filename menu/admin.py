from django.contrib import admin

# Register your models here.

from .models import MenuItem
from mptt.admin import MPTTModelAdmin


admin.site.register(MenuItem, MPTTModelAdmin)
