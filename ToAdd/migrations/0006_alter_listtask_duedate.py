# Generated by Django 4.0.4 on 2022-05-09 17:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToAdd', '0005_listtask_expired'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listtask',
            name='DueDate',
            field=models.DateField(blank=True, default=datetime.date.today),
        ),
    ]
