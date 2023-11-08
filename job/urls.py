from django.urls import path
from .views import job_list,job_detail,JobApply,AddJob
from .api import JobListAPI,JobDetailAPI


urlpatterns = [
    path('', job_list),
    path('add/', AddJob.as_view()),
    path('<slug:slug>',job_detail),
    path('<slug:slug>/apply',JobApply.as_view()),



    path('api/list', JobListAPI.as_view()),
    path('api/list/<int:pk>',JobDetailAPI.as_view()),
     
    
]
