from django.contrib import admin
from .models import address, pincode, cityID, countryID, stateID

# Register your models here.
admin.site.register(address)
admin.site.register(cityID)
admin.site.register(countryID)
admin.site.register(stateID)
admin.site.register(pincode)

