from django.contrib import admin
from .models import *


admin.site.register(ProjectType)

@admin.register(Projects)
class ProjectsAdmin(admin.ModelAdmin):
    list_display  = ['project_name','project_type','project_budget','project_manager','project_start_date','project_end_date']
    search_fields = ['project_name','project_type','project_manager']


@admin.register(Deliverables)
class DeliverablesAdmin(admin.ModelAdmin):
    list_display  = ['project','todo','completed']
    search_fields = ['project','completed']


admin.site.register(Status)
