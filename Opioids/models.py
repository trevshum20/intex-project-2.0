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

class pd_statedata(models.Model):
    state = models.CharField(max_length=20, null=True)
    stateabbrev = models.CharField(max_length=2, null=True, unique=True)
    population = models.IntegerField(null=True)
    deaths = models.IntegerField(null=True)
    class Meta:
        db_table = "pd_statedata"

    def __str__(self):
        return str(self.stateabbrev)
class Prescriber(models.Model):
    fname = models.CharField(max_length=50, null=True)
    lname = models.CharField(max_length=50, null=True)
    gender = models.CharField(max_length=1, null=True)
    state = models.ForeignKey(pd_statedata, on_delete=DO_NOTHING, to_field="stateabbrev")
    credential = models.CharField(max_length=20, null=True)
    specialty = models.ForeignKey(Specialty, on_delete=DO_NOTHING, null=True)
    isopioidprescriber = models.BooleanField(verbose_name='Opioid Prescriber',null=True)

    class Meta:
        db_table = "prescriber"

    def __str__(self):
        return (self.fname + ' ' + self.lname)

class Drug(models.Model):
    drugname = models.CharField(max_length=255, null=True)
    isopioid = models.BooleanField(verbose_name='Opioid')
    avg = models.IntegerField(null=True)
    class Meta:
        db_table = "pd_drugs"

    def __str__(self):
        return (self.drugname)

class Prescriber_Drug(models.Model):
    prescriber = models.ForeignKey(Prescriber, on_delete=DO_NOTHING)
    drug = models.ForeignKey(Drug, on_delete=DO_NOTHING)
    quantity = models.IntegerField(null=True)
    class Meta:
        db_table = "prescriber_drug"

    def __str__(self):
        return (str(self.prescriber) + ' ' + str(self.drug))

class Credentialz(models.Model):
    credentialz = models.CharField(max_length=255, null=True)
    class Meta:
        db_table = "credentialz"
    def __str__(self):
        return str(self.credentialz)




# class pd_prescriber(models.Model):
#     fname = models.CharField(max_length=11, null=True)
#     lname = models.CharField(max_length=11, null=True)
#     gender = models.CharField(max_length=1, null=True)
#     state = models.CharField(max_length=2, null=True)
#     credentials = models.CharField(max_length=20)
#     specialty = models.CharField(max_length=62, null=True)
#     isopioidprescriber = models.CharField(max_length=5, null=True)
#     totalprescriptions = models.IntegerField(null=True)

#     class Meta:
#         db_table = "pd_prescriber"
    
#     def __str__(self):
#         fullname = self.lname + ", " + self.fname
#         return fullname

# class pd_drugs(models.Model) :
#     drugname = models.CharField(max_length=30, null=True, unique=True)
#     isopioid = models.CharField(max_length=5, null=True)
#     class Meta:
#         db_table = "pd_drugs"
    
#     def __str__(self):
#         return self.drugname

# class pd_triple(models.Model):
#     prescriber = models.ForeignKey(pd_prescriber, to_field="id", on_delete=models.CASCADE, null=True)
#     drugname = models.ForeignKey(pd_drugs, to_field="drugname", on_delete=models.CASCADE, null=True)
#     qty = models.CharField(max_length=1, null=True)

#     class Meta:
#         db_table = "pd_triple"

#     def __str__(self):
#         return self.qty
