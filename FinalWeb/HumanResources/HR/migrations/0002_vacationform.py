# Generated by Django 4.2.1 on 2023-05-24 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='VacationForm',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('ID', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('fromDate', models.DateField()),
                ('toDate', models.DateField()),
                ('reason', models.TextField()),
                ('status', models.CharField(max_length=15)),
            ],
        ),
    ]
