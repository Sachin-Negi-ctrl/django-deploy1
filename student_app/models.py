from django.db import models
from tinymce.models import HTMLField

# Create your models here.
from django.db import models

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=500)
    duration = models.CharField(max_length=200)
    entry_qualification = models.CharField(max_length=500)
    intake = models.IntegerField()
    program_pattern = models.CharField(max_length=500)
    theory_practical_ratio = models.CharField(max_length=100)
    ecology_environment = models.CharField(max_length=500)
    entrepreneurship_development = models.CharField(max_length=500)
    industrial_exposure = models.CharField(max_length=500)
    discipline = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    



class CourseResult(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="results")
    session = models.CharField(max_length=10)  # Example: "2013-14"
    enrolled_students = models.PositiveIntegerField()
    passed_students = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.course.name} ({self.session})"




class PlacementRecord(models.Model):
    YEAR_CHOICES = [(r, str(r)) for r in range(2000, 2031)]  # Year range for selection

    year = models.IntegerField(choices=YEAR_CHOICES, default=2024)
    candidate_name = models.CharField(max_length=255)
    branch = models.CharField(max_length=50)
    company_name = models.CharField(max_length=255)
    package = models.FloatField(help_text="Package in Lakh per Annum")

    def __str__(self):
        return f"{self.candidate_name} - {self.company_name} ({self.year})"



class Topper(models.Model):
    name = models.CharField(max_length=255)
    year = models.CharField(max_length=20)
    marks_obtained = models.CharField(max_length=50)
    percentage = models.FloatField()
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="toppers", default=1)

    def __str__(self):
        return f"{self.name}"




class Subject(models.Model):
    SEMESTER_CHOICES = [
        ("1", "Semester 1"),
        ("2", "Semester 2"),
        ("3", "Semester 3"),
        ("4", "Semester 4"),
        ("5", "Semester 5"),
        ("6", "Semester 6"),
    ]

    name = models.CharField(max_length=255)
    semester = models.CharField(max_length=1, choices=SEMESTER_CHOICES)
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="subjects")

    def __str__(self):
        return f"{self.name} (Sem {self.semester}, {self.course.name})"

class PreviousPaper(models.Model):
    course = models.ForeignKey(Courses, on_delete=models.CASCADE, related_name="previous_papers")
    title = models.CharField(max_length=255)
    pdf_file = models.FileField(upload_to="previous_papers/")
    year = models.CharField(max_length=10)
    semester = models.CharField(max_length=1, choices=Subject.SEMESTER_CHOICES)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name="previous_papers")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} - {self.subject.name} (Sem {self.semester}, {self.year})"
    



class Facility(models.Model):
    title = models.CharField(max_length=255)  # Facility name
    description = HTMLField()  # Rich text field for details
    image1 = models.ImageField(upload_to='facilities/')
    image2 = models.ImageField(upload_to='facilities/')
    image3 = models.ImageField(upload_to='facilities/')
    image4 = models.ImageField(upload_to='facilities/')

    def __str__(self):
        return self.title
    

    