# Generated by Django 5.0.3 on 2024-03-13 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('time_tracker', '0004_task_timespend'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
