# Generated by Django 4.2.1 on 2023-05-25 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_rename_vfid_vacationform_employeeid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vacationform',
            old_name='EmployeeName',
            new_name='EmpName',
        ),
    ]