from django.db import models

# Create your models here.
class Logger(models.Model):
    Fisrt_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    time_log =  models.TimeField()
