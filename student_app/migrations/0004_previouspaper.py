# Generated by Django 5.1.6 on 2025-03-09 13:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0003_delete_previouspaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='previous_papers/')),
                ('year', models.CharField(max_length=10)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('subject', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=50)),
                ('paper_name', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_papers', to='student_app.courses')),
            ],
        ),
    ]
