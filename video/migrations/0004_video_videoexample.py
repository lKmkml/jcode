# Generated by Django 4.1.5 on 2023-02-13 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0003_videolesson_ordered'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='videoexample',
            field=models.FileField(blank=True, null=True, upload_to='video/example'),
        ),
    ]