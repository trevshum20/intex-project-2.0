from django.contrib import admin
from .models import pd_drugs, pd_prescriber, pd_statedata, pd_triple
# Register your models here.
admin.site.register(pd_prescriber)
admin.site.register(pd_triple)
admin.site.register(pd_drugs)
admin.site.register(pd_statedata)