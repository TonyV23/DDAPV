from django.db import models

class Province(models.Model) :
    
    province_name = models.CharField('Nom du province', max_length=20, help_text='taper le nom du province', unique = True)

    def __str__(self) -> str:
        return self.province_name
         
    
    class Meta : 
        ordering = ['province_name']