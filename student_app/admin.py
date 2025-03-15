from django.contrib import admin
from .models import * 

# Register your models here.


admin.site.register(Courses)


class CourseResultAdmin(admin.ModelAdmin):
    list_display = ('course', 'session', 'enrolled_students', 'passed_students') 
    list_filter = ('course',)  
    search_fields = ('session',)


admin.site.register(CourseResult, CourseResultAdmin)




@admin.register(PlacementRecord)
class PlacementRecordAdmin(admin.ModelAdmin):
    list_display = ("year", "candidate_name", "branch", "company_name", "package")
    list_filter = ("year", "branch", "company_name")
    search_fields = ("candidate_name", "company_name")



@admin.register(Topper)
class TopperAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'marks_obtained', 'percentage')
    list_filter = ('year', 'course')
    search_fields = ('name',)



@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ("name", "semester", "course")  # Display these columns
    list_filter = ("semester", "course")  # Filter sidebar
    search_fields = ("name",)  # Search bar for subjects

@admin.register(PreviousPaper)
class PreviousPaperAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "semester", "subject", "year", "uploaded_at")
    list_filter = ("course", "semester", "year", "subject")  # Filter sidebar
    search_fields = ("title", "year")  # Search by title and year
    ordering = ("-uploaded_at",)  # Newest papers first



@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    list_display = ('title',)