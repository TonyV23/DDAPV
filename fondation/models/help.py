from django.db import models

from fondation.models import TypeHelp

class Help (models.Model) : 
    
    type_help = models.ForeignKey(TypeHelp, on_delete=models.CASCADE)
    name = models.CharField("aides", max_length=40, unique=True, help_text='ex : vivre alimentaires , personnes vivant avec handicap')

    def __str__(self) -> str:
        return self.name

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['type_help', 'name'],
                name = 'unique_aide'
            )
        ]
        
        ordering = ['type_help', 'name']