from django.db import models
from student_app.models import Courses
# from ckeditor.fields import RichTextField
from tinymce.models import HTMLField



class GalleryImages(models.Model):
    image = models.ImageField(upload_to='gallery/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image {self.id}"



class Staff(models.Model):
    name = models.CharField(max_length=255)
    designation = models.CharField(max_length=255)
    qualification = models.CharField(max_length=255)
    image = models.ImageField(upload_to='staff/', blank=True, null=True)

    def get_image_url(self):
        if self.image:
            return self.image.url
        return 'college_web_app/static/images/default/staff.jpg'



    def __str__(self):
         return f"{self.name} - {self.designation}"
        


class CarouselImage(models.Model):
    image = models.ImageField(upload_to='carousel_images/')
    caption = models.CharField(max_length=255, blank=True, null=True)  # Optional caption
    created_at = models.DateTimeField(auto_now_add=True)  # To sort images by upload time

    def __str__(self):
        return f"Image {self.id} - {self.caption if self.caption else 'No Caption'}"



class CampusLifeImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to="campus_life/")
    is_featured = models.BooleanField(default=False)  # One image should be featured

    def __str__(self):
        return self.title



class Section(models.Model):
    title = models.CharField(max_length=100)  # "About Us", "Our Vision", "Our Mission"
    content = models.TextField()

    def __str__(self):
        return self.title



class Alumni(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact_no = models.CharField(max_length=15)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name='alumni')
    passing_year = models.PositiveIntegerField()
    company = models.CharField(max_length=200, blank=True, null=True)
    work_address = models.CharField(max_length=300, blank=True, null=True)
    designation = models.CharField(max_length=100, blank=True, null=True)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.passing_year})"
    



class ContactUs(models.Model):
    title = models.CharField(max_length=255, default="Contact Us")  # Static title
    description = HTMLField()  # Rich text field for details

    def __str__(self):
        return self.title  # Display title in admin 
    



class CollegeContent(models.Model):
    SECTION_CHOICES = [
        ('message', 'Message'),
        ('about', 'About GP Kotdwara'),
    ]
    
    section_type = models.CharField(max_length=10, choices=SECTION_CHOICES, unique=True)
    content = HTMLField()

    def __str__(self):
        return f"{self.get_section_type_display()}"




class FeeStructure(models.Model):
    title = models.CharField(max_length=225)
    pdf_file = models.FileField(upload_to='fee_structure/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title 
    

class Feature(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='features/images/')  # Thumbnail for the feature
    pdf_file = models.FileField(upload_to='features/pdfs/')  # PDF file
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title