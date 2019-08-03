from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    #listing_id = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    description = models.TextField(blank=True) #Optional
    price = models.IntegerField()
    bedroom = models.IntegerField()
    bathroom = models.DecimalField(max_digits=2, decimal_places=1)
    garage = models.IntegerField(default=0)
    list_date =  models.DateTimeField(default=datetime.now, blank=True)
    sqft = models.IntegerField()
    lot_size = models.DecimalField(max_digits=5, decimal_places=1)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True) #optional to upload image
    photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_two = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_three = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_four = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_five = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_six = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)

    # creating main field in admin area, in this case we are using title
    def __str__(self):
        return self.title