# Generated by Django 4.1.5 on 2023-01-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0010_donor_donation_received'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='sexe',
            field=models.CharField(choices=[('M', 'Masculin'), ('F', 'féminin')], max_length=20),
        ),
    ]