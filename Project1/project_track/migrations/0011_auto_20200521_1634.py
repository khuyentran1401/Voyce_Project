# Generated by Django 3.0.3 on 2020-05-21 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_track', '0010_profile_email_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='first_name',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='profile',
            name='last_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]