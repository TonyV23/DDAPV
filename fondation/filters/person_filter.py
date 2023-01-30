from django_filters import DateFilter, FilterSet, CharFilter

from fondation.models import Person

class PersonFilter(FilterSet) :

    start_date = DateFilter(field_name = 'date_joined', lookup_expr = 'gte')
    end_date = DateFilter(field_name = 'date_joined', lookup_expr = 'lte')
    keyword = CharFilter(field_name = 'nom_de_la_zone', lookup_expr = 'icontains')

    class Meta :
        model = Person
        fields = '__all__'
        exclude = [
            'nom', 'prenom', 'age','numero_de_telephone', 'nom_prenom_du_pere',
            'nom_prenom_de_la_mere', 'nom_de_la_zone','nombre_enfants','fonction', 'date_joined'
        ]