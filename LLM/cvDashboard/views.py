from django.shortcuts import render

def cv_page(request):
    return render(request, 'cvDashboard/job.html')