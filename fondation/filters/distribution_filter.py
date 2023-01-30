from django_filters import DateFilter, FilterSet, CharFilter

from fondation.models import Distribution

class DistributionFilter(FilterSet) :

    start_date = DateFilter(field_name = 'date_given', lookup_expr = 'gte')
    end_date = DateFilter(field_name = 'date_given', lookup_expr = 'lte')
    keyword = CharFilter(field_name = 'zone', lookup_expr = 'icontains')

    class Meta :
        model = Distribution
        fields = '__all__'
        exclude = [
            'zone','description', 'date_given'
            ]