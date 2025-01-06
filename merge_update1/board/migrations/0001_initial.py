# Generated by Django 5.1.4 on 2024-12-13 12:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('member', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('bno', models.AutoField(primary_key=True, serialize=False)),
                ('btitle', models.CharField(max_length=1000)),
                ('bcontent', models.TextField()),
                ('bgps', models.CharField(max_length=1000)),
                ('bselect', models.CharField(choices=[('생활/편의', '생활/편의🧼'), ('사건사고', '사건사고😈'), ('실시간공유', '실시간공유🗫'), ('감성카페', '감성카페☕'), ('취미', '취미🎮'), ('교통', '교통🚗'), ('웨이팅', '웨이팅👥'), ('기타', '기타🔍'), ('풍경', '풍경🌴'), ('추천맛집', '추천맛집😋')], max_length=500)),
                ('bgroup', models.IntegerField(null=True)),
                ('bstep', models.IntegerField(default=0)),
                ('bindent', models.IntegerField(default=0)),
                ('bhit', models.IntegerField(default=0)),
                ('bdate', models.DateTimeField(auto_now=True)),
                ('bfile', models.ImageField(blank=True, null=True, upload_to='board')),
                ('like_member', models.ManyToManyField(default='', related_name='like_member', to='member.member')),
                ('member', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='member.member')),
            ],
        ),
    ]