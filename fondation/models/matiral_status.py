from django.db import models

class MatiralStatus(models.Model) :
    
    situation_matrimoniale = models.CharField(max_length=20, help_text='renseignez la situation matrimoniale', unique= True)

    def __str__(self) -> str:
        return self.situation_matrimoniale