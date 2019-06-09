from uuid import uuid4
from django.db import models
from django.db.models import Sum
from dateutils import relativedelta
import datetime

GAS = 'GAS'
ELECTRICITY = 'ELECTRICITY'
READING_TYPES = [
    (ELECTRICITY, 'Electricity'),
    (GAS, 'Gas')
]


class UnitComplex(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    image = models.CharField(max_length=255, blank=True, null=False)

    @property
    def num_units(self):
        return Unit.objects.filter(unit_complex=self).count()


class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    bed_number = models.PositiveIntegerField()
    address = models.CharField(max_length=255, null=False, blank=False)
    unit_complex = models.ForeignKey(UnitComplex, on_delete=models.CASCADE)
    allowance = models.IntegerField(null=False, blank=False)


class MeterReading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    usage = models.FloatField(null=False, blank=False)
    reading_type = models.CharField(choices=READING_TYPES, max_length=32)
    multiplier = models.FloatField(blank=False, default=0.1)
    date = models.DateField(auto_now=False, auto_now_add=False)

    @property
    def charge(self):
        return self.multiplier*self.usage
