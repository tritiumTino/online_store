# Generated by Django 3.2.7 on 2021-10-23 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basketapp', '0002_auto_20211016_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='активно'),
        ),
    ]