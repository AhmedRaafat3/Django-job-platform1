import os , django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from faker import Faker
import random
from job.models import category, Company , job

def create_category(n):
    fake = Faker()
    for x in range(n):
        category.objects.create(
            name= fake.name()
        )
    print(f"{n} category was added succesfully")

def create_company(n):
     faker = Faker()
     images =['job-list1.png','job-list2.png','job-list3.png','job-list4.png']
     for x in range(n):
            Company.objects.create(
                 name=faker.company(),
                 website=faker.url(),
                 descrption=faker.text(),
                  location=random.choice(['New York','Los Angles','Chicago']),
                  email= faker.email(),
                  logo= f"company/{images[random.randint(0,3)]}"
          
    
                 
            )

     print(f"{n} company was added succesfully")    
          
         

def create_job(n):
     faker = Faker()
     job_type =['fulltime','parttime','remote','freelance']


     for x in range(n):
          job.objects.create(
               title= faker.name(),
               description = faker.sentence(),
               company=Company.objects.all().order_by('?')[0],
               vacancy= random.randint(2000,2500),
               salary_end=random.randint(2000,2500),
               location= random.randint(1,10),
               category= category.objects.all().order_by('?')[0],
               job_type= job_type[random.randint(0,3)]
        
          
          )
     print(f"{n} job was added succesfully")  
     
create_category(5)
create_company(100)
create_job(2000)

    

