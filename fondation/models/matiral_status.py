from django.db import models

class MatiralStatus(models.Model) :
    
    name = models.CharField('situation matrimoniale', max_length=20, help_text='tapez la situation matrimoniale', unique= True)

    def __str__(self) -> str:
        return self.name