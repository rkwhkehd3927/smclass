# Generated by Django 5.1.3 on 2024-12-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0007_rename_anumber_attendance_aticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendance',
            name='usedTicket',
            field=models.IntegerField(default=0),
        ),
    ]