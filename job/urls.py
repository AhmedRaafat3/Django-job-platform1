from django.urls import path
from .views import job_list,job_detail
from .api import JobListAPI,JobDetailAPI


urlpatterns = [
    path('', job_list),
    path('<slug:slug>',job_detail),



    path('api/list', JobListAPI.as_view()),
    path('api/list/<int:id>',JobDetailAPI.as_view),
    
]
