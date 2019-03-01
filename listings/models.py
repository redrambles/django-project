from django.db import models
from datetime import datetime
from realtors.models import Realtor

# Don't need an id field - that is automatic
class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True) #This field is optional
  price = models.IntegerField()
  bedroooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1) # Ex: 1.5
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1) # Ex: 2.4 acres
  photo_main = models.ImageField(upload_to='photos/%Y/%M/%d/')
  photo_1 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
  photo_2 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
  photo_3 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
  photo_4 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
  photo_5 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
  photo_6 = models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title # This is to set the main field for the admin