# Generated by Django 5.0.6 on 2024-06-13 00:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0029_alter_volunteer_volunteer_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='volunteerrole',
            name='date_entered',
        ),
    ]