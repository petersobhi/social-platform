# Generated by Django 3.2.5 on 2021-07-09 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_like_unique_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.BigIntegerField(default=0),
        ),
    ]
