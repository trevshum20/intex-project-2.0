from django.contrib import admin
from .models import Specialty, Prescriber, Drug, Prescriber_Drug
# Register your models here.
admin.site.register(Specialty)
admin.site.register(Prescriber)
admin.site.register(Drug)
admin.site.register(Prescriber_Drug)