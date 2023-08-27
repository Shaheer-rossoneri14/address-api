from django.contrib import admin
from .models import address, countryCode, state, city, pincode

# Register your models here.
admin.site.register(address)
admin.site.register(countryCode)
admin.site.register(state)
admin.site.register(city)
admin.site.register(pincode)

