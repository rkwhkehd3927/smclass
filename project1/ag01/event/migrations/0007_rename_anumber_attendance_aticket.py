# Generated by Django 5.1.3 on 2024-12-06 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0006_attendance_anumber'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='aNumber',
            new_name='aTicket',
        ),
    ]