# Generated by Django 3.0.3 on 2020-08-13 14:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('AboutName', models.CharField(max_length=40)),
                ('AboutImage', models.URLField(unique=True)),
                ('AboutEmail', models.EmailField(max_length=20, unique=True)),
                ('AboutPhone', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999999)])),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('eventDate', models.DateField()),
                ('eventName', models.CharField(max_length=40)),
                ('eventImage', models.URLField(unique=True)),
                ('eventRegistration', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resourcetDate', models.DateField()),
                ('resourceName', models.CharField(max_length=40)),
                ('resourceImage', models.URLField(unique=True)),
                ('resourceFeedback', models.URLField(unique=True)),
            ],
        ),
    ]
