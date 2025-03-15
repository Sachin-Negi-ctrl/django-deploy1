from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    search_fields = ('title',)


@admin.register(Aicte_files)
class AicteFiles(admin.ModelAdmin):
    list_display = ('title', 'published_at',)
    search_fields = ('title',)


@admin.register(OrganizationChart)
class OrganizationChartAdmin(admin.ModelAdmin):
    list_display = ('title','pdf_file', 'uploaded_at')