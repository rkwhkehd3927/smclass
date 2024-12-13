# Generated by Django 5.1.3 on 2024-12-08 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_alter_member_agree1_alter_member_agree2_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('verification_email', models.EmailField(max_length=254)),
                ('verification_code', models.CharField(max_length=6)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
