"""govrent URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from govrent.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/complex', ListComplexes.as_view()),
    path('v1/complex/<uuid:complex_id>', ComplexDetailView.as_view()),
    path('v1/complex/<uuid:complex_id>/units', ComplexUnitsDetailView.as_view()),
    path('v1/unit', ListUnits.as_view()),
    path('v1/unit/<uuid:id>', UnitDetailView.as_view()),
    path('v1/unit/<uuid:unit_id>/readings/gas', GasMeterReadingDetailView.as_view()),
    path('v1/unit/<uuid:unit_id>/readings/electricity', ElectricityMeterReadingDetailView.as_view()),
    path('v1/unit/<uuid:unit_id>/readings/total', TotalMeterReadingDetailView.as_view()),
    path('v1/unit/<uuid:unit_id>/readings/gas/monthly', GasMeterReadingMonthlyDetailView.as_view()),
    path('v1/unit/<uuid:unit_id>/readings/electricity/monthly', ElectricityMeterReadingMonthlyDetailView.as_view()),
    path('v1/unit/<uuid:unit_id>/readings/total/monthly', TotalMeterReadingMonthlyDetailView.as_view()),
]
