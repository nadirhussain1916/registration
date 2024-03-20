from django.db import models
from django.contrib.auth.models import User

class User(models.Model):
    username=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    password1=models.CharField(max_length=20)
    # password2=models.CharField(max_length=20)

    # class Meta:
    #     db_table='app1_user'
    #     model=User
        # fields=['username', 'email', 'password1', 'password2']
# Create your models here.
