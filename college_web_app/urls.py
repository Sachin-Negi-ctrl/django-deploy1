from django.urls import path, include
from .views import *
from django.conf import settings

from django.conf.urls.static import static


urlpatterns = [
    path('', index,  name='home'),
    path('courses/', courses, name='courses'),                       
    path('result/', result, name='result'), 
    path('gallery/', gallery_view, name='gallery'),  
    path('placements/', placement_records, name="placement_records"),     
    path('staff/', staff_records, name="staff_records"),
    path('toppers/', topper_list, name='topper_list'),   
    path('student/', include('student_app.urls')),     
    path('campus-life/', campus_life, name='campus_life'),
    path('register/', alumni_register, name='alumni_register'),
    path('members/', alumni_list, name='alumni_list'),
    path('contact/', contact_us, name='contact_us'),
    
] 


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)