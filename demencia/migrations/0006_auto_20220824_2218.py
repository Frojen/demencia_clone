# Generated by Django 3.2.9 on 2022-08-24 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demencia', '0005_alter_mappoint_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='mappoint',
            name='description',
            field=models.CharField(default='', max_length=100, verbose_name='Описание'),
        ),
        migrations.AddField(
            model_name='mappoint',
            name='opening_hours',
            field=models.CharField(default='', max_length=100, verbose_name='Время работы'),
        ),
    ]
