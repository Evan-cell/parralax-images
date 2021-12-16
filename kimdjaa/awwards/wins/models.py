from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
# Create your models here.
#Projects model
class Projects(models.Model): 
  project_owner = models.ForeignKey(User,on_delete=models.CASCADE)
  name = models.CharField(max_length=100)
  description = models.TextField(max_length=400)
  main_technology_used = models.CharField(max_length=30,null=True)
  screenshot = CloudinaryField('screenshot')
  live_link = models.URLField(max_length=100)
  date_added = models.DateField(auto_now_add=True)
  
  def save_project(self): 
    '''Function to save a project'''
    self.save()
  
  def __str__(self):
    return self.name 
