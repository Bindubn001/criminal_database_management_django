from django.contrib import admin

# Register your models here.
from .models import Crime,Prison,Criminal,Victim,Trial
admin.site.register(Crime)
admin.site.register(Prison)
admin.site.register(Criminal)
admin.site.register(Victim)
admin.site.register(Trial)

