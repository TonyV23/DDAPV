# Generated by Django 4.1.5 on 2023-01-13 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0003_matiralstatus'),
    ]

    operations = [
        migrations.CreateModel(
            name='LevelStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('niveau_etudes', models.CharField(help_text="tapez le niveau d'études", max_length=30, unique=True)),
            ],
        ),
    ]
