from django.db import models

# Create your models here.
class signup(models.Model):
    username=models.CharField(max_length=25)
    password=models.CharField(max_length=20)



class signin(models.Model):
    username=models.ForeignKey(signup,on_delete=models.CASCADE , related_name='uesr')
    password=models.ForeignKey(signup,on_delete=models.CASCADE , related_name='passworld')


