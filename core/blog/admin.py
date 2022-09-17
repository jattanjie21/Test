from django.contrib import admin
from .models import *


admin.site.register(Category)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display  = ['title','category','publish','created_at']
    search_fields = ['title','category']
    list_filter   = ['title','category','publish']


