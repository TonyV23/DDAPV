from django.db import models

class Camp (models.Model) :
    
    nom_du_camp = models.CharField(max_length=100, unique=True,help_text="tapez le nom du camp d'intervetion")
    site = models.CharField(max_length=100, help_text="tapez la localisation géograpfique du camp où se trouve ce camp")

    def __str__(self) -> str:
        return self.nom_du_camp+''+self.site

    class Meta :
        constraints = [
            models.UniqueConstraint(
                fields= ['nom_du_camp', 'site'],
                name = 'unique_camp'
            )
        ]