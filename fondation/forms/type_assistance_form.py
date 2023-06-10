from django.forms import ModelForm

from fondation.models import TypeAssistance

class TypeAssistanceForm(ModelForm) :

    class Meta :
        model = TypeAssistance
        fields = '__all__'