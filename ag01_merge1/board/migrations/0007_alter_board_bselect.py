# Generated by Django 5.1.3 on 2024-12-05 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_board_like_member_alter_board_bselect'),
    ]

    operations = [
        migrations.AlterField(
            model_name='board',
            name='bselect',
            field=models.CharField(choices=[('실시간공유', '실시간공유🗫'), ('취미', '취미🎮'), ('웨이팅', '웨이팅👥'), ('풍경', '풍경🌴'), ('생활/편의', '생활/편의🧼'), ('교통', '교통🚗'), ('사건사고', '사건사고😈'), ('감성카페', '감성카페☕'), ('기타', '기타🔍'), ('추천맛집', '추천맛집😋')], max_length=500),
        ),
    ]
