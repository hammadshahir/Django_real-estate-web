from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    realtor_name = models.CharField(max_length=200)
    realtor_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    realtor_description = models.TextField(blank=True)
    realtor_email = models.EmailField(max_length=50)
    realtor_phone = models.CharField(max_length=20)
    is_mvp = models.BooleanField(default=False)
    hired_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.realtor_name