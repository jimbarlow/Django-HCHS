# Generated by Django 5.0.6 on 2024-05-17 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0012_delete_volunteerroles_remove_volunteerrole_volunteer'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteerrole',
            name='volunteer_role_description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='volunteerrole',
            name='volunteer_role',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]