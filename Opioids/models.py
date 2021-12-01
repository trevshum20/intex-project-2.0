from django.db import models
from django.db.models.fields import NOT_PROVIDED, GenericIPAddressField

# Create your models here.

class pd_prescriber(models.Model):
    fname = models.CharField(max_length=11, null=True)
    lname = models.CharField(max_length=11, null=True)
    gender = models.CharField(max_length=1, null=True)
    state = models.CharField(max_length=2, null=True)
    credentials = models.CharField(max_length=20)
    specialty = models.CharField(max_length=62, null=True)
    isopioidprescriber = models.CharField(max_length=5, null=True)
    totalprescriptions = models.IntegerField(null=True)

    class Meta:
        db_table = "pd_prescriber"
    
    def __str__(self):
        fullname = self.lname + ", " + self.fname
        return fullname

class pd_drugs(models.Model) :
    drugname = models.CharField(max_length=30, null=True, unique=True)
    isopioid = models.CharField(max_length=5, null=True)
    class Meta:
        db_table = "pd_drugs"
    
    def __str__(self):
        return self.drugname

class pd_triple(models.Model):
    prescriber = models.ForeignKey(pd_prescriber, to_field="id", on_delete=models.CASCADE, null=True)
    drugname = models.ForeignKey(pd_drugs, to_field="drugname", on_delete=models.CASCADE, null=True)
    qty = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = "pd_triple"

    def __str__(self):
        return self.qty

class pd_statedata(models.Model):
    state = models.CharField(max_length=20, null=True)
    stateabbrev = models.CharField(max_length=2, null=True)
    population = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    class Meta:
        db_table = "pd_statedata"

    def __str__(self):
        return str(self.deaths)

        