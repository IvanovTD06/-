from django.db import models

class TRF(models.Model):
    Name = models.CharField(max_length=36)
    Surname = models.CharField(max_length=36)
    Surname1 = models.CharField(max_length=36)

class DRF(models.Model):
    Discipline_name = models.CharField(max_length=48)

class ERF(models.Model):
    Equipment_name = models.CharField(max_length=64)

class BRF(models.Model):
    Building_name = models.CharField(max_length=48)

class CTRF(models.Model):
    Cabinet_type_name = models.CharField(max_length=32)

class CRF(models.Model):

    Building = models.CharField(max_length=48, choices = [("Ильинка", "Ильинка"), ("Речная", "Речная")])
    Cabinet_number = models.IntegerField()
    Cabinet_type = models.CharField(max_length=96)
    Equipment = models.CharField(max_length=96)


class Connection_data(models.Model):
    db_name = models.CharField(max_length=32, choices=(("", ""), ("postgres", "postgres")))
    db_user = models.CharField(max_length=48, choices=(("", ""), ("student", "student")))
    db_password = models.CharField(max_length=32, choices=(("", ""), ("123456", "123456")))
    db_host = models.CharField(max_length=32, choices=(("", ""), ("localhost", "localhost")))
    db_port = models.IntegerField()