# Generated by Django 5.1.6 on 2025-03-12 06:38

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0010_subject_previouspaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', tinymce.models.HTMLField()),
                ('image1', models.ImageField(upload_to='facilities/')),
                ('image2', models.ImageField(upload_to='facilities/')),
                ('image3', models.ImageField(upload_to='facilities/')),
                ('image4', models.ImageField(upload_to='facilities/')),
            ],
        ),
    ]
