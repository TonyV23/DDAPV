from django_filters import DateFilter, FilterSet, CharFilter

from fondation.models import Donor

class DonorFilter(FilterSet) :

    start_date = DateFilter(field_name = 'donor_date_given', lookup_expr = 'gte')
    end_date = DateFilter(field_name = 'donor_date_given', lookup_expr = 'lte')
    keyword = CharFilter(field_name = 'donor_date_given', lookup_expr = 'icontains')

    class Meta :
        model = Donor
        fields = '__all__'
        exclude = [
            'numero_de_telephone', 'adresse_mail',
            'description', 'donor_date_given'
        ]