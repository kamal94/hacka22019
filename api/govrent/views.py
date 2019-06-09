from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import authentication, permissions
from govrent.models import *
from govrent.serializers import *
import datetime
from dateutils import relativedelta

class ListComplexes(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        """
        Return a list of all complexes.
        """
        complexes = UnitComplex.objects.all()
        print(complexes)
        serializer = UnitComplexSerializer(complexes, many=True)
        print(serializer.data)
        return Response(
            serializer.data,
            headers={
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "*"
            })

    
    def post(self, request):
        """
        Creates a new complex.
        """
        serializer = UnitComplexSerializer(request.data)
        serializer.save()
        return Response(serializer.data)


class ComplexDetailView(APIView):
    """
    View to get a complex in the.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, complex_id):
        """
        Return Complex by id.
        """
        unit_complex = UnitComplex.objects.get(pk=complex_id)
        serializer = UnitComplexSerializer(unit_complex)
        return Response(serializer.data)

class ComplexUnitsDetailView(APIView):
    """
    View to get a complex in the.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, complex_id):
        """
        Return Complex by id.
        """
        units = Unit.objects.filter(unit_complex=complex_id)
        serializer = UnitSerializer(units, many=True)
        return Response(serializer.data)



class ListUnits(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request):
        """
        Return a list of all units.
        """
        units = Unit.objects.all()
        serializer = UnitSerializer(units, many=True)
        
        return Response(serializer.data)
    
    def post(self, request):
        """
        Creates a new complex.
        """
        serializer = UnitSerializer(request.data)
        serializer.save()
        return Response(
            serializer.data
        )


class UnitDetailView(APIView):
    """
    View to get a units with an id.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, id):
        """
        Return unit by id.
        """
        unit = Unit.objects.get(pk=id)
        serializer = UnitSerializer(unit)
        return Response(serializer.data)



class MeterReadingUnitDetailView(APIView):
    """
    View to get a units with an id.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, unit_id):
        """
        Return unit by id.
        """
        start_date = request.GET.get(
            'start_date',
            datetime.datetime.now() - relativedelta(years=1)
        ) or datetime.datetime.now() - relativedelta(years=1)
        end_date = request.GET.get(
            'end_date',
            datetime.datetime.now()
        ) or datetime.datetime.now()
        reading_type = str(request.GET.get(
            'reading_type',
            ''
        )).upper()
        print(reading_type)
        if reading_type:
            readings = MeterReading.objects.filter(
                unit=unit_id,
                date__gte=start_date,
                date__lte=end_date,
                reading_type=reading_type
                )
        else:
            readings = MeterReading.objects.filter(
                unit=unit_id,
                date__gte=start_date,
                date__lte=end_date
                )
        serializer = MeterReadingSerializer(readings, many=True)
        return Response(serializer.data)


class MeterReadingUnitMonthlyDetailView(APIView):
    """
    View to get a units with an id.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    # permission_classes = (permissions.IsAdminUser,)

    def get(self, request, unit_id):
        """
        Return unit by id.
        """
        start_date = request.GET.get(
            'start_date',
            datetime.datetime.now() - relativedelta(years=1)
        ) or datetime.datetime.now() - relativedelta(years=1)
        start_date = start_date.replace(day=1)
        end_date = request.GET.get(
            'end_date',
            datetime.datetime.now()
        ) or datetime.datetime.now()
        start_date = start_date.replace(day=1)

        reading_type = str(request.GET.get(
            'reading_type',
            ''
        )).upper()

        months = {}
        while(start_date < end_date):
            if reading_type:
                first_of_month = start_date.replace(day=1)
                last_of_month = start_datereplace(day=1) + relativedelta(months=1) - relativedelta(days=1)
                readings_sum = MeterReading.objects.filter(
                    date__gte=first_of_month,
                    date__lte=last_of_month,
                    reading_type=reading_type
                ).aggregate(Sum('usage'))
                months[start_date.strftime("%Y-%m-%d")] = round(readings_sum['usage__sum'], 0)
            else:

                first_of_month = start_date.replace(day=1)
                last_of_month = start_date.replace(day=1) + relativedelta(months=1) - relativedelta(days=1)
                readings_sum = MeterReading.objects.filter(
                    date__gte=first_of_month,
                    date__lte=last_of_month,
                ).aggregate(Sum('usage'))
                months[start_date.strftime("%Y-%m-%d")] = round(readings_sum['usage__sum'], 0)
            
            start_date += relativedelta(months=1)
        return JsonResponse(months, safe=False)
