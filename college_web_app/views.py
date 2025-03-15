from django.shortcuts import render, HttpResponse, redirect 
from .models import *
from file_storing_app.models import *
from .forms import *
from student_app.models import *
# Create your views here.

def index(request):
    # Fetch the latest organization chart PDF
    latest_chart = OrganizationChart.objects.order_by('-uploaded_at').first()

    # Fetch other required data
    carousel_images = CarouselImage.objects.all()
    notices = Notice.objects.order_by('-published_at')
    files_aicte = Aicte_files.objects.order_by('-published_at')
    images = CampusLifeImage.objects.all()[:5]
    featured_image = CampusLifeImage.objects.filter(is_featured=True).first()
    other_images = CampusLifeImage.objects.filter(is_featured=False)[:4]
    sections = Section.objects.all()
    message = CollegeContent.objects.filter(section_type='message').first()
    about = CollegeContent.objects.filter(section_type='about').first()
    fee_struct = FeeStructure.objects.order_by('-uploaded_at').first()
    features = Feature.objects.order_by('-uploaded_at')[:6] 

    return render(request, 'college_web_app/home.html', {
        "images": images,
        "carousel_images": carousel_images,
        "notices": notices,
        "files_aicte": files_aicte,
        "featured_image": featured_image,
        "other_images": other_images,
        "sections": sections,
        "latest_chart": latest_chart,  # Pass organization chart to template
        "message": message,
        "about": about,
        "fee_struct": fee_struct,
        "features": features,
    })
 

def courses(request):
    courses = Courses.objects.all()
    return render(request, 'college_web_app/courses.html', {'courses':courses})



def result(request):
    # Fetch all course results ordered by course and session
    course_results = CourseResult.objects.select_related('course').order_by('course', 'session')

    # Organize results by course
    courses = {}
    for result in course_results:
        if result.course not in courses:
            courses[result.course] = []
        courses[result.course].append(result)

    return render(request, 'college_web_app/course_result.html', {'courses': courses})



def gallery_view(request):
    images = GalleryImages.objects.all()
    return render(request, 'college_web_app/gallery.html', {'images': images})




def placement_records(request):
    selected_year = request.GET.get('year')  # Get year from the dropdown selection
    years = PlacementRecord.objects.values_list('year', flat=True).distinct().order_by('-year')

    if selected_year:
        records = PlacementRecord.objects.filter(year=selected_year)
    else:
        records = PlacementRecord.objects.all()

    return render(request, 'college_web_app/placement.html', {'records': records, 'years': years, 'selected_year': selected_year})  



def staff_records(request):
    staff_members = Staff.objects.all()
    return render(request,"college_web_app/staff.html",{"staff_members":staff_members})



def topper_list(request):
    selected_course_id = request.GET.get('course', '')
    selected_year = request.GET.get('year', '')

    # Fetch all courses
    courses = Courses.objects.all()

    # Dictionary to store toppers grouped by course
    toppers_by_course = {}

    # If a course is selected, filter toppers for that specific course
    if selected_course_id:
        selected_course = Courses.objects.get(id=selected_course_id)
        toppers = Topper.objects.filter(course=selected_course)
        if selected_year:
            toppers = toppers.filter(year=selected_year)

        if toppers.exists():
            toppers_by_course[selected_course] = toppers
    else:
        # If no course is selected, show all toppers grouped by course
        for course in courses:
            toppers = Topper.objects.filter(course=course)
            if selected_year:
                toppers = toppers.filter(year=selected_year)

            if toppers.exists():
                toppers_by_course[course] = toppers

    years = Topper.objects.values_list('year', flat=True).distinct()

    return render(request, 'college_web_app/topper_list.html', {
        'toppers_by_course': toppers_by_course,
        'courses': courses,
        'years': years,
        'selected_course_id': selected_course_id,
        'selected_year': selected_year
    })



def campus_life(request):
    images = CampusLifeImage.objects.all()[:5]  # Fetch only 5 images
    featured_image = CampusLifeImage.objects.filter(is_featured=True).first()  # Fetch the featured image
    other_images = CampusLifeImage.objects.filter(is_featured=False)[:4]  # Get 4 other images

    return render(request, 'college_web_app/campus_life.html', {
        'featured_image': featured_image,
        'other_images': other_images
    })





def alumni_register(request):
    if request.method == "POST":
        form = AlumniForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('alumni_list')
    else:
        form = AlumniForm()
    return render(request, 'college_web_app/register.html', {'form': form})

def alumni_list(request):
    alumni_members = Alumni.objects.all().order_by('-passing_year')
    return render(request, 'college_web_app/list.html', {'alumni_members': alumni_members})



def contact_us(request):
    contact_info = ContactUs.objects.first()  # Get the first entry (only one should exist)
    return render(request, 'college_web_app/contact.html', {'contact_info': contact_info})


