from django.db import models

class TypeHelp(models.Model) :

    name = models.CharField("type d'aides", max_length=40, unique=True, help_text='ex : aides en nature , aides en espece')

    def __str__(self) -> str:
        return self.name