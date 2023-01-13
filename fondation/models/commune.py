from django.db import models

from fondation.models import Province

class Commune(models.Model) : 
    
    province_name = models.ForeignKey(Province, on_delete=models.CASCADE)
    commune_name = models.CharField(max_length=20, help_text='tapez le nom de la commune', unique=True)

    def __str__(self) -> str:
        return self.commune_name +', '+self.province_name

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['province_name', 'commune_name'],
                name = 'unique_commune'
            )
        ]