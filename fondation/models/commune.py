from django.db import models

from fondation.models import Province

class Commune(models.Model) : 
    
    nom_de_la_province = models.ForeignKey(Province, on_delete=models.CASCADE)
    nom_de_la_commune = models.CharField(max_length=20, help_text='tapez le nom de la commune', unique=True)

    def __str__(self) -> str:
        return self.nom_de_la_commune +', '+self.nom_de_la_province

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields = ['nom_de_la_province','nom_de_la_commune'],
                name = 'unique_commune'
            )
        ]