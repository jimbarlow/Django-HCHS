# Generated by Django 5.0.6 on 2024-06-04 01:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0013_volunteerrole_volunteer_role_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='volunteerrole',
            old_name='volunteer_role',
            new_name='vol_role',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='volunteerrole',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='volunteer.volunteerrole'),
        ),
    ]
