# Generated by Django 4.2.11 on 2024-05-14 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0010_tickets'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerRoles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('role_description', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
