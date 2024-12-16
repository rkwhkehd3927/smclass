# Generated by Django 5.1.4 on 2024-12-15 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0002_alter_board_bselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bselect',
            field=models.CharField(choices=[('추천맛집', '추천맛집😋'), ('감성카페', '감성카페☕'), ('취미', '취미🎮'), ('웨이팅', '웨이팅👥'), ('생활/편의', '생활/편의🧼'), ('교통', '교통🚗'), ('기타', '기타🔍'), ('사건사고', '사건사고😈'), ('실시간공유', '실시간공유🗫'), ('풍경', '풍경🌴')], max_length=500),
        ),
    ]
