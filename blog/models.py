from django.db import models

class BlogArticle(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateField()
    text= models.CharField(max_length=250)
# Create your models here.
