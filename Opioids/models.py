from django.db import models
from django.db.models.deletion import DO_NOTHING

# Create your models here.
class Specialty (models.Model):
    specialty = models.CharField(max_length=255, null=True)
    weight = models.IntegerField(null=True, default=0)

    class Meta:
        db_table = "specialty"

    def __str__(self):
        return (self.specialty)


class Prescriber(models.Model):
    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, null=True)
    state = models.CharField(max_length=2, null=True)
    credential = models.CharField(max_length=20, null=True)
    specialty = models.ForeignKey(Specialty, on_delete=DO_NOTHING, null=True)

    class Meta:
        db_table = "prescriber"

    def __str__(self):
        return (self.fname + ' ' + self.lname)

class Drug(models.Model):
    drugname = models.CharField(max_length=255, null=True)
    isopioid = models.BooleanField(verbose_name='Opioid')

    class Meta:
        db_table = "drug"

    def __str__(self):
        return (self.drugname)

class Prescriber_Drug(models.Model):
    prescriber = models.ForeignKey(Prescriber, on_delete=DO_NOTHING)
    drug = models.ForeignKey(Drug, on_delete=DO_NOTHING)
    quantity = models.IntegerField(null=True)
    class Meta:
        db_table = "prescriber_drug"

    def __str__(self):
        return (self.prescriber + ' ' + self.drug)