# Generated by Django 5.0.6 on 2024-06-05 03:33

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0015_remove_volunteer_volunteerrole_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='volunteerrole',
            name='volunteer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='volunteer.volunteer'),
        ),
    ]