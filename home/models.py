from django.db import models

# Create your models here.


class Visit(models.Model):
    fromdate = models.CharField(max_length=30)
    todate = models.CharField(max_length=30)
    noofguest = models.CharField(max_length=30)
    typeofacc = models.TextField()
