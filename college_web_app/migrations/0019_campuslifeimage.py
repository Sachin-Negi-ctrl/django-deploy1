# Generated by Django 5.1.6 on 2025-03-09 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college_web_app', '0018_remove_courseresult_course_remove_topper_course_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CampusLifeImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='campus_life/')),
                ('is_featured', models.BooleanField(default=False)),
            ],
        ),
    ]
