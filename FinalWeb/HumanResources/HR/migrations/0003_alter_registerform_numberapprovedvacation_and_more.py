# Generated by Django 4.2.1 on 2023-05-31 17:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_registeredvacationform'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerform',
            name='NumberApprovedVacation',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='registerform',
            name='NumberVacation',
            field=models.IntegerField(),
        ),
    ]
