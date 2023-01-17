from django.forms import ModelForm

from fondation.models import Distribution

class DistributionForm(ModelForm) :

    class Meta :
        model = Distribution
        fields = '__all__'