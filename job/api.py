from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework import generics
from .serializers import JobSerializer
from .models import job

#@api_view(['GET'])
#def job_list_api(request):
 #   jobs = job.objects.all()
  #  data = JobSerializer(jobs, many=True).data
   # return Response({'Jobs':data})

#@api_view(['GET'])
#def job_detail_api(request,id):
 #   job1= job.objects.get(id=id)
  #  data=JobSerializer(job1).data
  #  return Response({'Job':data})


class JobListAPI(generics.ListCreateAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer 
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['title', 'vacancy','job_type']
    search_fields =['title',' description']
    ordering_fields = ['salary_start', 'salary_end',' experience']
    permission_classes = [IsAuthenticated]



class JobDetailAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer 

