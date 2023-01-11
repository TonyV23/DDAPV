from django.db import models

class LevelStudy(models.Model) : 
    
    level_study_name = models.CharField("Niveau d'études", max_length=30, help_text = "tapez le niveau d'études", unique=True)

    def __str__(self) -> str:
        return self.level_study_name