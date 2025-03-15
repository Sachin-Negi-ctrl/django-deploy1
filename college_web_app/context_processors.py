from file_storing_app.models import Aicte_files, OrganizationChart
from college_web_app.models import FeeStructure

def aicte_files_processor(request):
    files_aicte = Aicte_files.objects.order_by('-published_at')
    return {"files_aicte": files_aicte}


def org_chart_processor(request):
    latest_chart = OrganizationChart.objects.order_by('-uploaded_at').first()
    return {"latest_chart": latest_chart}

def fee_struct_processor(request):
    fee_struct = FeeStructure.objects.order_by('-uploaded_at').first()
    return {"fee_struct": fee_struct}