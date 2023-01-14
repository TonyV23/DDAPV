from django.forms import ModelForm

from fondation.models import LevelStudy

class LevelStudyForm(ModelForm) :

    class Meta :
        model = LevelStudy
        fields = '__all__'