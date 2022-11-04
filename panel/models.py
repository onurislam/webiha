from django.db import models


# Create your models here.
class IHA(models.Model):
    title = models.CharField(max_length=100)
    model = models.CharField(max_length=80)
    category = models.CharField(max_length=80)
    weight = models.IntegerField()
    images = models.FileField(null=True, blank=True)
