from django.db import models
from django.db.models.fields import NOT_PROVIDED, GenericIPAddressField

# Create your models here.

class pd_prescriber(models.Model):
    NPI = models.IntegerField(null=True, unique=True)
    Fname = models.CharField(max_length=11, null=True)
    Lname = models.CharField(max_length=11, null=True)
    Gender = models.CharField(max_length=1, null=True)
    State = models.CharField(max_length=2, null=True)
    Credential = models.CharField(max_length=20)
    Specialty = models.CharField(max_length=62, null=True)
    IsOpioidPrescriber = models.CharField(max_length=5, null=True)
    TotalPrescriptions = models.IntegerField(null=True)

    class Meta:
        db_table = "pd_prescriber"
    
    def __str__(self):
        fullname = self.Lname + ", " + self.Fname
        return fullname

class pd_drugs(models.Model) :
    DrugName = models.CharField(max_length=30, null=True, unique=True)
    IsOpioid = models.CharField(max_length=5, null=True)
    class Meta:
        db_table = "pd_drugs"
    
    def __str__(self):
        return self.DrugName
class pd_triple(models.Model):
    PrescriberID = models.ForeignKey(pd_prescriber, to_field="NPI", on_delete=models.CASCADE, null=True)
    DrugName = models.ForeignKey(pd_drugs, to_field="DrugName", on_delete=models.CASCADE, null=True)
    Qty = models.CharField(max_length=1, null=True)

    class Meta:
        db_table = "pd_triple"

    def __str__(self):
        return self.Qty