from __future__ import unicode_literals
from django.db import models


# Create your models here.
class Gym(models.Model):
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=400)

    # votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name + ": " + self.address


class Members(models.Model):
    gym = models.ForeignKey(Gym, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    vorname = models.CharField(max_length=200)
    uuid = models.CharField(max_length=200, unique=True)
    join_date = models.DateField('joined date', null=True)

    def __str__(self):
        return '{} {} - {}'.format(self.vorname, self.name, self.gym)
