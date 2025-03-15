from django.db import models
from django.utils import timezone 
# Create your models here.
class Notice(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    pdf_file = models.FileField(upload_to='notices/')  # Uploads to MEDIA_ROOT/notices/
    published_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title




class Aicte_files(models.Model):
    title = models.CharField(max_length=200)
    pdf_file = models.FileField(upload_to='aicte_files/')
    published_at = models.DateTimeField(auto_now_add=True)  # Fix default value

    def __str__(self):
        return self.title
    

class OrganizationChart(models.Model):
    title = models.CharField(max_length=225)
    pdf_file = models.FileField(upload_to='organization_chart/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Organization Chart ({self.uploaded_at.strftime('%Y-%m-%d')})"