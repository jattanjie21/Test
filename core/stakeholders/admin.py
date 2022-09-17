from django.contrib import admin
from .models import *


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):
    list_display  = ['name', 'type_of_stakeholder', 'website', 'email', 'address', 'country', 'active']
    list_filter   = ['type_of_stakeholder', 'active']
    search_fields = ['name', 'type_of_stakeholder', 'website', 'email', 'address', 'country', 'active']
    list_per_page = 25
