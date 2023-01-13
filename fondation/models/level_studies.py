from django.db import models

class LevelStudy(models.Model) : 
    
    niveau_etudes = models.CharField(max_length=30, help_text = "tapez le niveau d'études", unique=True)

    def __str__(self) -> str:
        return self.niveau_etudes