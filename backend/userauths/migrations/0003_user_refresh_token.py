# Generated by Django 4.2.7 on 2024-10-11 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_alter_user_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='refresh_token',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
