# Generated by Django 5.0.7 on 2024-07-19 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('venue', models.CharField(max_length=200)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='activity_photos/')),
                ('video', models.FileField(blank=True, null=True, upload_to='activity_videos/')),
            ],
        ),
    ]