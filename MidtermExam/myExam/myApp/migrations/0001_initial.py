# Generated by Django 5.1.6 on 2025-03-05 00:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('description', models.TextField(max_length=250)),
                ('due_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.TextField(max_length=100)),
            ],
        ),
    ]
