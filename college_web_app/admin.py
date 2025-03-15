from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(GalleryImages)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_thumbnail', 'uploaded_at')
    list_filter = ('uploaded_at',)
    search_fields = ('id',)
    readonly_fields = ('image_thumbnail',)

    def image_thumbnail(self, obj):
        from django.utils.html import format_html
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto; border-radius: 5px;" />', obj.image.url)
        return "No Image"

    image_thumbnail.short_description = "Preview"


@admin.register(Staff) 
class StaffAdmin(admin.ModelAdmin):
    list_display = ("name", "designation")
    search_fields = ("name",)



@admin.register(CarouselImage)
class CarouselImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'caption', 'created_at')  # Show details in the admin panel





@admin.register(CampusLifeImage)
class CampusLifeImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_featured')


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ("title",)  # Show titles in the admin list
    search_fields = ("title",)  # Enable search by title



@admin.register(Alumni)
class AlumniAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'course', 'passing_year', 'company', 'contact_no', 'designation']
    list_filter = ['course', 'passing_year']
    search_fields = ['name', 'email', 'company']


admin.site.register(ContactUs)


# admin.site.register(CollegeContent)
@admin.register(CollegeContent)
class CollegeContentAdmin(admin.ModelAdmin):
    list_display = ('section_type', 'content')


admin.site.register(FeeStructure) 


@admin.register(Feature)
class FeatureAdmin(admin.ModelAdmin):
    list_display = ('title', 'uploaded_at')
    search_fields = ('title',)