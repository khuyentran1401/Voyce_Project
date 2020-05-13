# Generated by Django 3.0.6 on 2020-05-12 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_track', '0002_auto_20200512_0041'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('user_id', models.IntegerField(auto_created=True, db_index=True, primary_key=True, serialize=False, unique=True)),
                ('user_name', models.CharField(max_length=30)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=60)),
                ('user_password', models.CharField(max_length=60)),
            ],
        ),
    ]
