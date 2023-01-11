from django.db import models

class TypeHelp(models.Model) :

    type_help_name = models.CharField("type d'aide", max_length=40, unique=True, help_text='ex : aides en nature , aides en espece')

    def __str__(self) -> str:
        return self.type_help_name