# Generated by Django 3.0.4 on 2020-03-29 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0008_auto_20200328_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='boomer',
            name='distance',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='zoomer',
            name='distance',
            field=models.FloatField(default=0),
        ),
    ]
