from django.contrib import admin
from .models import Mapping


@admin.register(Mapping)
class MappingAdmin(admin.ModelAdmin):
    list_display = 'name', 'latitude', 'longitude', 'expiration_date'

