from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from.models import job , JobApply

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




class JobApply(CreateView):
     model = JobApply
     success_url = '/jobs/'
     fields=[' username','email','Link_url',' github_url',' cv','cover_lette']

     def form_valid(self, form):
         slug= self.kwargs.get('slug')
         job= get_object_or_404(job,slug=slug)
         job_apply=form.save(commit=False)
         job_apply.job=job
         job_apply.save()

         return super().form_valid(form)
     