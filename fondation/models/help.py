from django.db import models

from fondation.models import TypeHelp

class Help (models.Model) : 
    
    type_help_name = models.ForeignKey(TypeHelp, on_delete=models.CASCADE)
    help_name = models.CharField("aides", max_length=40, unique=True, help_text='ex : vivre alimentaires , personnes vivant avec handicap')

    def __str__(self) -> str:
        return self.help_name+', '+self.type_help_name

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['type_help_name', 'help_name'],
                name = 'unique_aide'
            )
        ]