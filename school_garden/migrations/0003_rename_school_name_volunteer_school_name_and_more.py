# Generated by Django 4.1 on 2022-08-24 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_garden', '0002_volunteer_school_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteer',
            old_name='School_name',
            new_name='school_name',
        ),
        migrations.AlterField(
            model_name='school',
            name='school_name',
            field=models.CharField(max_length=150),
        ),
    ]
