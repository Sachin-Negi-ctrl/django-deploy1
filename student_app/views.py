from django.shortcuts import render
from .models import *


# Create your views here.
def courses(request):
    courses = Courses.objects.all()
    return render(request, 'student_app/courses.html', {'courses':courses})
 

def result(request):
    # Fetch all course results ordered by course and session
    course_results = CourseResult.objects.select_related('course').order_by('course', 'session')

    # Organize results by course
    courses = {}
    for result in course_results:
        if result.course not in courses:
            courses[result.course] = []
        courses[result.course].append(result)

    return render(request, 'student_app/course_result.html', {'courses': courses})




def placement_records(request):
    selected_year = request.GET.get('year')  # Get year from the dropdown selection
    years = PlacementRecord.objects.values_list('year', flat=True).distinct().order_by('-year')

    if selected_year:
        records = PlacementRecord.objects.filter(year=selected_year)
    else:
        records = PlacementRecord.objects.all()

    return render(request, 'student_app/placement.html', {'records': records, 'years': years, 'selected_year': selected_year})  




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

    return render(request, 'student_app/topper_list.html', {
        'toppers_by_course': toppers_by_course,
        'courses': courses,
        'years': years,
        'selected_course_id': selected_course_id,
        'selected_year': selected_year
    })
    


def previous_papers_list(request):
    courses = Courses.objects.all()
    subjects = Subject.objects.all()
    semester_choices = Subject.SEMESTER_CHOICES  # Pass Semester Choices

    # Get selected filters
    selected_course = request.GET.get('course', '')
    selected_year = request.GET.get('year', '')
    selected_semester = request.GET.get('semester', '')
    selected_subject = request.GET.get('subject', '')

    papers = PreviousPaper.objects.all()

    # Apply filters
    if selected_course:
        papers = papers.filter(course_id=selected_course)

    if selected_year:
        papers = papers.filter(year=selected_year)

    if selected_semester:
        papers = papers.filter(semester=selected_semester)

    if selected_subject:
        papers = papers.filter(subject_id=selected_subject)

    return render(request, "student_app/previous_papers.html", {
        "papers": papers,
        "courses": courses,
        "subjects": subjects,
        "semester_choices": semester_choices,  # Pass semester choices
        "selected_course": selected_course,
        "selected_year": selected_year,
        "selected_semester": selected_semester,
        "selected_subject": selected_subject,
    })



def facilities_view(request):
    facilities = Facility.objects.all()
    return render(request, 'student_app/facilities.html', {'facilities': facilities})

