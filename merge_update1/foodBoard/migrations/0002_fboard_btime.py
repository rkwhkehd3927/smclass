# Generated by Django 5.1.4 on 2024-12-13 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBoard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fboard',
            name='bTime',
            field=models.CharField(choices=[(0, '바로 입장'), (10, '10분 이내'), (30, '30분 이내'), (60, '1시간 이상'), (120, '2시간 이상'), (45, '30분~1시간')], default=0, max_length=200),
            preserve_default=False,
        ),
    ]
