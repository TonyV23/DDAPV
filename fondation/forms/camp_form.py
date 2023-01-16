from django.forms import ModelForm

from fondation.models import Camp

class CampForm(ModelForm) :

    class Meta :
        model = Camp
        fields = '__all__'