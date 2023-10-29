from django.contrib import admin
from .models import category,Company,job

class jobAdmin(admin.ModelAdmin):
    list_display=['title','location','company','job_type','vacancy','category']
    search_fields=('title','category','description')
    list_filter=('vacancy','job_type','category','experience')


admin.site.register(job,jobAdmin)
admin.site.register(Company)
admin.site.register(category)

# Register your models here.
