# Generated by Django 4.1.5 on 2023-01-26 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0020_distribution_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='description',
            field=models.TextField(blank=True, help_text="reseignez autre type d'assistance qui ne figure pas dans la liste", max_length=500),
        ),
    ]