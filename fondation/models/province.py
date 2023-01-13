from django.db import models

class Province(models.Model) :
    
    nom_province = models.CharField(max_length=20, help_text='taper le nom du province', unique = True)

    def __str__(self) -> str:
        return self.nom_province
         
    
    class Meta : 
        ordering = ['nom_province']