from django.forms import ModelForm

from fondation.models import Province

class ProvinceForm (ModelForm) : 

    class Meta : 
        model = Province
        fields = '__all__'