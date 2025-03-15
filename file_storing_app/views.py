from django.shortcuts import render
from .models import *

def notice_list(request):
    notices = Notice.objects.order_by('-published_at')  # Show latest first
    return render(request, 'file_storing_app/notices.html', {'notices': notices})

