from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from.models import job

def job_list(request):
    aLL_Jobs= job.objects.all()
    jobs_count= aLL_Jobs.count()
    page = request.GET.get('page', 1)
    paginator = Paginator( aLL_Jobs, 50)
    try:
         aLL_Jobs = paginator.page(page)
    except PageNotAnInteger:
         aLL_Jobs= paginator.page(1)
    except EmptyPage:
          aLL_Jobs = paginator.page(paginator.num_pages)
    return render(request,'job/job_list.html',{'jobs':aLL_Jobs,' jobs_count': jobs_count})


def job_detail(request,slug):
    Job =job.objects.get(slug=slug)
    return render (request,'job/job_detail.html',{'Job':Job})