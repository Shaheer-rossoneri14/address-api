from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class countryCode(models.Model):
    id = models.BigAutoField(primary_key=True)
    iso_id = models.CharField(max_length=3, unique=True, blank=None)


class state(models.Model):
    id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=100, blank=None)


class city(models.Model):
    id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=100, blank=None)


class pincode(models.Model):
    id = models.BigAutoField(primary_key=True)
    pin_code = models.CharField(max_length=15, unique=True)


class address(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.TextField()
    line2 = models.TextField()
    pin_code = models.ForeignKey(pincode, on_delete=models.CASCADE)
    home_city = models.ForeignKey(city, on_delete=models.CASCADE)
    home_state = models.ForeignKey(state, on_delete=models.CASCADE)
    home_country = models.ForeignKey(countryCode, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=True)





