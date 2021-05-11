from django.db import models
from django.db.models import Model
from django.contrib.auth.models import User



# Create your models here.


class BlogModel(models.Model):
    title= models.CharField(max_length=1000)
    content= models.TextField()
    user=models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    image= models.ImageField(upload_to='blog')

   
  


    
def __str__(self):
    return self.title



    
        






