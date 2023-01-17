from django.forms import ModelForm

from fondation.models import Person

class RefugeeForm (ModelForm) :

    class Meta :
        model = Person
        fields = '__all__'