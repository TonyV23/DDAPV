# Generated by Django 4.1.5 on 2023-01-17 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fondation', '0013_alter_donor_donor_date_given'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distribution',
            name='date_given',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
