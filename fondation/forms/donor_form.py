from django.forms import ModelForm

from fondation.models import Donor

class DonorForm( ModelForm) :

    class Meta :
        model = Donor
        fields = '__all__'