from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password1=models.CharField(max_length=20)




class Post(models.Model):
    text = models.TextField()
    # image = models.ImageField(upload_to='uploads/')
    image = models.ImageField(upload_to='images')

    # updated_by=models.ForeignKey(User, related_name='updated_by_user', on_delete=models.CASCADE)
    # created_by=models.ForeignKey(User, related_name='created_by_user', on_delete=models.CASCADE)
    # created_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.text[:50]  

