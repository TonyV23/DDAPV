# Generated by Django 4.1.5 on 2023-01-17 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0014_alter_distribution_date_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='age',
            field=models.DateField(verbose_name='date de naissance'),
        ),
    ]
