# Generated by Django 3.0.4 on 2020-03-28 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0007_auto_20200328_1802'),
    ]

    operations = [
        migrations.AddField(
            model_name='boomer',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='zoomer',
            name='address',
            field=models.CharField(default='', max_length=100),
        ),
    ]
