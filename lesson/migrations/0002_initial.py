# Generated by Django 5.1.7 on 2025-03-30 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lesson', '0001_initial'),
        ('module', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lesson',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lessons', to='module.module'),
        ),
    ]
