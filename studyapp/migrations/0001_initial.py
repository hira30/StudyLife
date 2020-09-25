# Generated by Django 2.2.5 on 2020-09-22 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StudyLifeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日付')),
                ('time', models.DecimalField(decimal_places=2, default=0.0, max_digits=2, verbose_name='勉強時間')),
                ('task', models.CharField(max_length=20, null=True, verbose_name='学習内容')),
                ('memo', models.TextField(verbose_name='メモ')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='ユーザー')),
            ],
        ),
    ]
