from django.contrib import admin
from .models import Project, Client, ProjectManager, EngineerRequirement

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('project_name', 'location', 'region', 'project_start_date', 'project_end_date')
    list_filter = ('region', 'project_start_date', 'project_end_date')
    search_fields = ('project_name', 'location')
    
@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_contact_name', 'client_contact_number', 'client_contact_email')
    search_fields = ('client_contact_name', 'client_contact_number', 'client_contact_email')

@admin.register(ProjectManager)
class ProjectManagerAdmin(admin.ModelAdmin):
    list_display = ('project_manager_id', 'project_manager_title', 'project_manager_name', 'project_manager_email', 'project_head_count')
    list_filter = ('project_manager_title',)
    search_fields = ('project_manager_name', 'project_manager_id', 'project_manager_email')

@admin.register(EngineerRequirement)
class EngineerRequirementAdmin(admin.ModelAdmin):
    list_display = ('band', 'head_count')
    list_filter = ('band', 'head_count')
