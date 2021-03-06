# Generated by Django 3.0.4 on 2020-03-28 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('details', models.TextField(max_length=100)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Zoomer',
            fields=[
                ('username', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=200)),
                ('surname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('postal_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.RemoveField(
            model_name='boomer',
            name='id',
        ),
        migrations.AddField(
            model_name='boomer',
            name='email',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boomer',
            name='password',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='boomer',
            name='username',
            field=models.CharField(default='', max_length=50, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
