# Generated by Django 2.2.5 on 2020-09-22 07:24

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0002_auto_20200922_1520'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaskModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AlterField(
            model_name='studylifemodel',
            name='task',
            field=models.CharField(max_length=30, null=True, verbose_name='学習内容'),
        ),
        migrations.AlterField(
            model_name='studylifemodel',
            name='time',
            field=models.DecimalField(decimal_places=1, default=0.0, max_digits=3, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(24.0)], verbose_name='学習時間'),
        ),
    ]
