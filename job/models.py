from django.db import models
from django_countries.fields import CountryField
from django.utils import timezone
from django.utils.text import slugify

JOB_TYPE=(

    ('fulltime','fulltime'),
    ('parttime','parttime'),
    ('remote','remote'),
    ('freelance','freelance'),
)
class job(models.Model):
    title = models.CharField(max_length=120)
    location = CountryField()
    company = models.ForeignKey('Company',on_delete=models.CASCADE,related_name='job_company')
    created_at = models.DateTimeField(default=timezone.now)
    salary_start= models.IntegerField(null=True,blank=True)
    salary_end= models.IntegerField(null=True,blank=True)
    description=models.TextField(max_length=15000)
    vacancy=models.IntegerField()
    job_type=models.CharField(choices= JOB_TYPE,max_length=10)
    experience=models.IntegerField()
    category=models.ForeignKey('category',related_name='job_category',on_delete=models.SET_NULL,null=True,blank=True)
    slug=models.SlugField(null=True,blank=True)

    def __str__(self):
        return self.title
    

class category(models.Model):
     name= models.CharField(max_length=30)
     logo= models.CharField(max_length=30,null=True,blank=True)

     def __str__(self):
        return self.name
     
     def save(self, *args, **kwargs):
         self.slug = slugify(self.name)
         super(category, self).save(*args, **kwargs)


class Meta:
    ordering=['-id']
    

class Company(models.Model):
    name = models.CharField(max_length=50)
    logo = models.ImageField(upload_to='company')
    subtitle = models.TextField(max_length=1000)
    website = models.URLField()
    email = models.EmailField()

    def __str__(self):
        return self.name
    
class JobApply(models.Model):
    job=models.ForeignKey(job,related_name='apply_job',on_delete=models.CASCADE)
    username=models.CharField(max_length=100)
    email=models.EmailField()
    Link_url=models.URLField(null=True,blank=True,help_text='please enter your linkedin profile url')
    github_url=models.URLField(null=True,blank=True,help_text='please enter your github profile url')
    cv=models.FileField(upload_to='cv',help_text='please upload your latest cv')
    cover_letter=models.TextField(max_length=500,help_text='add your nodes here....')
    created_at = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return self.username
