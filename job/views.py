from django.shortcuts import render
from.models import job

def job_list(request):
    aLL_Jobs= job.objects.all()
    return render(request,'job/job_list.html',{'jobs':aLL_Jobs})
