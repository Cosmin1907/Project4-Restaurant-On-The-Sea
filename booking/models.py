from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Table(models.Model):
    table_number = models.IntegerField()
    capacity = models.IntegerField()
    notes = models.TextField(blank=True) # Field for staff notes

