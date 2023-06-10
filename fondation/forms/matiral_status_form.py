from django.forms import ModelForm

from fondation.models import MatiralStatus

class MatiralStatusForm(ModelForm) :

    class Meta :
        model = MatiralStatus
        fields = '__all__'