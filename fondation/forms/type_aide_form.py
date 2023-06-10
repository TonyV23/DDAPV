from django.forms import ModelForm

from fondation.models import TypeAide

class TypeAideForm(ModelForm) :

    class Meta :
        model = TypeAide
        fields = '__all__'