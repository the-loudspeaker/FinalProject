# Generated by Django 2.0.5 on 2018-07-29 18:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180729_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='created',
            field=models.DateTimeField(verbose_name=datetime.datetime(2018, 7, 29, 18, 24, 52, 186945, tzinfo=utc)),
        ),
    ]