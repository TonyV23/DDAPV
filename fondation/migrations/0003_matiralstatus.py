# Generated by Django 4.1.5 on 2023-01-10 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0002_commune_commune_unique_commune'),
    ]

    operations = [
        migrations.CreateModel(
            name='MatiralStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='tapez la situation matrimoniale', max_length=20, unique=True, verbose_name='situation matrimoniale')),
            ],
        ),
    ]
