# Generated by Django 4.1 on 2022-08-24 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school_garden', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='School_name',
            field=models.CharField(default='Enter School Name', max_length=150),
        ),
    ]
