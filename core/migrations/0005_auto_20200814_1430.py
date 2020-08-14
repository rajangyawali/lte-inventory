# Generated by Django 2.2 on 2020-08-14 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200814_1037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='employeeinformation',
            options={'ordering': ['employee_id'], 'verbose_name_plural': 'NT Employees'},
        ),
        migrations.AlterModelOptions(
            name='site',
            options={'ordering': ['-added_on'], 'verbose_name_plural': 'Sites'},
        ),
        migrations.AlterField(
            model_name='site',
            name='site_id',
            field=models.CharField(max_length=8, unique=True, verbose_name='Site ID'),
        ),
    ]