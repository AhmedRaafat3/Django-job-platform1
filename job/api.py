from rest_framework.decorators import api_view
from rest_framework.response import Response
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


class JobListAPI(generics.ListAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer 



class JobDetailAPI(generics.RetrieveAPIView):
    queryset = job.objects.all()
    serializer_class = JobSerializer 

