# Generated by Django 5.1.6 on 2025-03-09 13:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0007_delete_previouspaper'),
    ]

    operations = [
        migrations.CreateModel(
            name='PreviousPaper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('pdf_file', models.FileField(upload_to='previous_papers/')),
                ('year', models.CharField(max_length=10)),
                ('semester', models.CharField(choices=[('1', 'Semester 1'), ('2', 'Semester 2'), ('3', 'Semester 3'), ('4', 'Semester 4'), ('5', 'Semester 5'), ('6', 'Semester 6')], max_length=1)),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='previous_papers', to='student_app.courses')),
            ],
        ),
    ]
