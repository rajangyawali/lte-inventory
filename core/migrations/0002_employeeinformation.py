# Generated by Django 2.2 on 2020-08-14 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_name', models.CharField(max_length=100, verbose_name='Employee Name')),
                ('employee_address', models.CharField(blank=True, max_length=200, null=True, verbose_name='Employee Address')),
                ('employee_mobile', models.CharField(max_length=10, verbose_name='Mobile Number')),
                ('employee_landline', models.CharField(blank=True, max_length=9, null=True, verbose_name='Landline Number')),
                ('employee_id', models.PositiveIntegerField(verbose_name='Employee ID')),
                ('team_added_on', models.DateTimeField(auto_now_add=True, verbose_name='Added On')),
                ('team_updated_on', models.DateTimeField(auto_now=True, verbose_name='Updated On')),
            ],
            options={
                'verbose_name_plural': 'NT Employees',
            },
        ),
    ]