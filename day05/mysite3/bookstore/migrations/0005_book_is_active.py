# Generated by Django 2.2.12 on 2022-02-01 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0004_auto_20220129_1141'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_active',
            field=models.BooleanField(default=True, verbose_name='是否活跃'),
        ),
    ]
