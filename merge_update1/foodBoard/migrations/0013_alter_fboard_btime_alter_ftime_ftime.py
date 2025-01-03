# Generated by Django 5.1.4 on 2024-12-27 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodBoard', '0012_alter_fboard_btime_alter_ftime_ftime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fboard',
            name='bTime',
            field=models.CharField(choices=[(60, '1시간 이상'), (0, '바로 입장'), (120, '2시간 이상'), (30, '30분 이내'), (45, '30분~1시간'), (10, '10분 이내')], max_length=200),
        ),
        migrations.AlterField(
            model_name='ftime',
            name='fTime',
            field=models.IntegerField(choices=[(60, '1시간 이상'), (0, '바로 입장'), (120, '2시간 이상'), (30, '30분 이내'), (45, '30분~1시간'), (10, '10분 이내')]),
        ),
    ]
