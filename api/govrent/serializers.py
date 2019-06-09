from rest_framework import serializers
from govrent.models import *

class UnitComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitComplex
        fields = ('id', 'address', 'num_units', 'image')
    

class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'bed_number', 'address', 'unit_complex', 'allowance')

class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = ('id', 'unit', 'usage', 'reading_type', 'date', 'charge')