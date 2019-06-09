from uuid import uuid4
from django.db import models

GAS = 'GAS'
ELECTRICITY = 'ELECTRICITY'
READING_TYPES = [
    (ELECTRICITY, 'Electricity'),
    (GAS, 'Gas')
]

class Complex(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    address = models.CharField(max_length=255, null=False, blank=False)

    @property
    def num_units(self):
        return Unit.objects.filter(complex=self)


class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    bed_number = models.PositiveIntegerField()
    complex = models.ForeignKey(Complex, on_delete=models.CASCADE)

class MeterReading(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)
    reading_type = models.CharField(choices=READING_TYPES, max_length=32)
    date = models.DateField(auto_now=False, auto_now_add=False)