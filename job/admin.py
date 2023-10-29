from django.contrib import admin
from .models import category,Company,job


admin.site.register(job)
admin.site.register(Company)
admin.site.register(category)

# Register your models here.
