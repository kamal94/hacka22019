from rest_framework import serializers
from govrent.models import *

class UnitComplexSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnitComplex
        fields = ('id', 'address', 'num_units')
    
    def create(self, validated_data):
        return UnitComplex.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.address)
        instance.save()
        return instance


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unit
        fields = ('id', 'bed_number', 'address', 'unit_complex', 'allowance')

    def create(self, validated_data):
        return Unit.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.address = validated_data.get('address', instance.email)
        instance.bed_number = validated_data.get('bed_number', instance.bed_number)
        instance.unit_complex = validated_data.get('unit_complex', instance.unit_complex)
        instance.save()
        return instance

class MeterReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeterReading
        fields = ('id', 'unit', 'usage', 'reading_type', 'date')

    def create(self, validated_data):
        return MeterReading.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.unit = validated_data.get('unit', instance.unit)
        instance.usage = validated_data.get('usage', instance.usage)
        instance.reading_type = validated_data.get('reading_type', instance.reading_type)
        instance.date = validated_data.get('date', instance.date)
        instance.save()
        return instance
        