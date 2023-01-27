from django.db import models

from fondation.models import TypeAide

class TypeAssistance(models.Model) :
    
    type_aide = models.ForeignKey(TypeAide, on_delete=models.CASCADE)
    type_assistance = models.CharField(max_length=100, unique = True)

    def __str__(self) -> str:
        return self.type_assistance
    
    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['type_aide','type_assistance'],
                name = 'unique_type_assistance'
            )
        ]