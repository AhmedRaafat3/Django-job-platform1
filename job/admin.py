from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import category,Company,job, JobApply

class jobAdmin(SummernoteModelAdmin):
    list_display=['title','location','company','job_type','vacancy','category']
    search_fields=('title','category','description')
    list_filter=('vacancy','job_type','category','experience')
    summernote_fields = '__all__'


admin.site.register(job,jobAdmin)
admin.site.register(Company)
admin.site.register(category)
admin.site.register(JobApply)

# Register your models here.
