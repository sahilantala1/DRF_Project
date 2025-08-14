import django_filters
from DRF_App.models import *

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')

    class Meta:
        model = Employee_details
        fields = ['designation']