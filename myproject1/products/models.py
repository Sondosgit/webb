from django.db import models

class Product(models.Model):
    pname = models.CharField(max_length=64)
    desc = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField(upload_to="photos/%y/%m/%d")

    def __str__(self):
        return self.pname
    
    
