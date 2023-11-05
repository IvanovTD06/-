from django.db import models

class TRF(models.Model):
    Name = models.CharField(max_length=36)
    Surname = models.CharField(max_length=36)
    Surname1 = models.CharField(max_length=36)

class DRF(models.Model):
    Discipline_name = models.CharField(max_length=48)

class SRF(models.Model):
    Subject_name = models.CharField(max_length=64)

class BRF(models.Model):
    Building_name = models.CharField(max_length=48)

class CTRF(models.Model):
    Cabinet_type_name = models.CharField(max_length=32)