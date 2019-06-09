from rest_framework.views import APIView
from django.http.response import JsonResponse
from rest_framework.response import Response
from rest_framework import authentication, permissions
from govrent.models import *
from govrent.serializers import *
import datetime
from dateutils import relativedelta


def get_end_date(request):
    end_date = request.GET.get(
        'end_date',
        datetime.datetime.now()
    ) or datetime.datetime.now()
    if not isinstance(end_date, datetime.datetime):
        end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d')
    return end_date.replace(day=1)


def get_start_date(request):
    start_date = request.GET.get(
        'start_date',
        datetime.datetime.now() - relativedelta(years=1)
    ) or datetime.datetime.now() - relativedelta(years=1)
    if not isinstance(start_date, datetime.datetime):
        start_date = datetime.datetime.strptime(start_date, '%Y-%m-%d')

    return start_date.replace(day=1)


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


class TotalMeterReadingDetailView(APIView):
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
        start_date = get_start_date(request)
        end_date = get_end_date(request)    
        readings = MeterReading.objects.filter(
            unit=unit_id,
            date__gte=start_date,
            date__lte=end_date
        )
        result = []
        while(start_date < end_date):
            # add elec and water
            day_readings = list(filter(
                lambda x: datetime.datetime(year=x.date.year, month=x.date.month, day=x.date.day) == start_date,
                readings
            ))
            print(day_readings)
            if len(day_readings) == 2:
                total_reading = {
                    "unit": str(day_readings[0].unit.id),
                    "charge": day_readings[0].charge + day_readings[1].charge,
                    "date": day_readings[0].date
                }
                result.append(total_reading)
            start_date += relativedelta(days=1)
        return JsonResponse(result, safe=False)


class ElectricityMeterReadingDetailView(APIView):
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
        start_date = get_start_date(request)
        end_date = get_end_date(request)
        readings = MeterReading.objects.filter(
            unit=unit_id,
            date__gte=start_date,
            date__lte=end_date,
            reading_type='ELECTRICITY'
        )
        serializer = MeterReadingSerializer(readings, many=True)
        return Response(serializer.data)


class GasMeterReadingDetailView(APIView):
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
        start_date = get_start_date(request)
        end_date = get_end_date(request)
        readings = MeterReading.objects.filter(
            unit=unit_id,
            date__gte=start_date,
            date__lte=end_date,
            reading_type='GAS'
        )
        serializer = MeterReadingSerializer(readings, many=True)
        return Response(serializer.data)



class GasMeterReadingMonthlyDetailView(APIView):
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
        start_date = get_start_date(request)
        end_date = get_end_date(request)
        months = {}
        while(start_date <= end_date):
            first_of_month = start_date.replace(day=1)
            last_of_month = start_date.replace(
                day=1) + relativedelta(months=1) - relativedelta(days=1)
            readings_sum = MeterReading.objects.filter(
                date__gte=first_of_month,
                date__lte=last_of_month,
                unit=unit_id,
                reading_type='GAS'
            ).aggregate(Sum('usage'))
            months[start_date.strftime(
                "%Y-%m-%d")] = round(readings_sum['usage__sum']*.06, 0)
            start_date += relativedelta(months=1)
        return JsonResponse(months, safe=False)


class ElectricityMeterReadingMonthlyDetailView(APIView):
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
        start_date = get_start_date(request)
        end_date = get_end_date(request)
        months = {}
        while(start_date <= end_date):
            first_of_month = start_date.replace(day=1)
            last_of_month = start_date.replace(
                day=1) + relativedelta(months=1) - relativedelta(days=1)
            readings_sum = MeterReading.objects.filter(
                date__gte=first_of_month,
                date__lte=last_of_month,
                unit=unit_id,
                reading_type='ELECTRICITY'
            ).aggregate(Sum('usage'))
            months[start_date.strftime(
                "%Y-%m-%d")] = round(readings_sum['usage__sum']*.06, 0)
            start_date += relativedelta(months=1)
        return JsonResponse(months, safe=False)


class TotalMeterReadingMonthlyDetailView(APIView):
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
        start_date = get_start_date(request)
        end_date = get_end_date(request)
        months = {}
        while(start_date <= end_date):
            first_of_month = start_date.replace(day=1)
            last_of_month = start_date.replace(
                day=1) + relativedelta(months=1) - relativedelta(days=1)
            readings_sum = MeterReading.objects.filter(
                date__gte=first_of_month,
                date__lte=last_of_month,
                unit=unit_id
            ).aggregate(Sum('usage'))
            months[start_date.strftime(
                "%Y-%m-%d")] = round(readings_sum['usage__sum']*.06, 0)
            start_date += relativedelta(months=1)
        return JsonResponse(months, safe=False)
