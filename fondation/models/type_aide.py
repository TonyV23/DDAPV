from django.db import models

class TypeAide(models.Model) :
    
    type_aide = models.CharField(max_length=20, unique = True)

    def __str__(self) -> str:
        return self.type_aide