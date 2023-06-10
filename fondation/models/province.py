from django.db import models

class Province(models.Model) :
    
    nom_de_la_province = models.CharField(max_length=20, help_text='taper le nom de la province', unique = True)

    def __str__(self) -> str:
        return self.nom_de_la_province