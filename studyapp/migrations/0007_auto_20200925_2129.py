# Generated by Django 2.2.5 on 2020-09-25 12:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0006_auto_20200923_2121'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='studylifemodel',
            name='unique_task',
        ),
        migrations.AlterField(
            model_name='studylifemodel',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 9, 25, 21, 29, 49, 717194), verbose_name='日付'),
        ),
    ]