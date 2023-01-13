from django.forms import ModelForm

from fondation.models import Province

class ProvinceForm (ModelForm) : 

    class Meta : 
        model = Province
        fields = '__all__'
        labels = {
            'nom_de_la_province' : 'nom province origine'
        } 