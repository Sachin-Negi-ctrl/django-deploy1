from django.urls import path
from .views import *

urlpatterns = [

    path('courses/', courses, name='courses'),                       
    path('result/', result, name='result'), 
    path('placements/', placement_records, name="placement_records"),    
    path('toppers/', topper_list, name='topper_list'),   
    path('prev-paper', previous_papers_list, name="previous_papers"),
    path('facilities/', facilities_view, name='facilities'),

  
] 
 