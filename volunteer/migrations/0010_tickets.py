# Generated by Django 4.2.11 on 2024-05-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('volunteer', '0009_volunteerrole_date_entered_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_path', models.CharField(max_length=300)),
            ],
        ),
    ]
