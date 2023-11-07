from django.db import models
import psycopg2
from psycopg2 import OperationalError


def create_connection(db_name, db_user, db_password, db_host, db_port):
        connection = None
        try:
            connection = psycopg2.connect(
                database=db_name,
                user=db_user,
                password=db_password,
                host=db_host,
                port=db_port,
            )
            print("Connection to PostgreSQL DB successful")
        except OperationalError as e:
            print(f"The error '{e}' occurred")
        return connection

def reader(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except OperationalError as e:
        print(f"The error '{e}' occurred")


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
    Building = models.CharField(max_length=48)
    Cabinet_number = models.IntegerField()
    Cabinet_type = models.CharField(max_length=96)
    Equipment = models.CharField(max_length=96)
    
    