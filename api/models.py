from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class countryID(models.Model):
    country_id = models.CharField(primary_key=True, max_length=3)
    country_name = models.CharField(max_length=100)

    def __str__(self):
        return self.country_name


class stateID(models.Model):
    state_id = models.BigAutoField(primary_key=True)
    state_name = models.CharField(max_length=100)
    country_id = models.ForeignKey(countryID, on_delete=models.CASCADE)

    def __str__(self):
        return self.state_name


class cityID(models.Model):
    city_id = models.BigAutoField(primary_key=True)
    city_name = models.CharField(max_length=100)
    state_id = models.ForeignKey(stateID, on_delete=models.CASCADE)

    def __str__(self):
        return self.city_name


class pincode(models.Model):
    pin_code = models.CharField(primary_key=True, max_length=15, unique=True)

    def __str__(self):
        return self.pin_code


class address(models.Model):
    id = models.BigAutoField(primary_key=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    line1 = models.TextField()
    line2 = models.TextField()
    city = models.ForeignKey(cityID, on_delete=models.CASCADE)
    state = models.ForeignKey(stateID, on_delete=models.CASCADE)
    country = models.ForeignKey(countryID, on_delete=models.CASCADE)
    pin_code = models.ForeignKey(pincode, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    is_default = models.BooleanField(default=True)