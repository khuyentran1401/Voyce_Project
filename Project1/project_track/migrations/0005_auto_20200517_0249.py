# Generated by Django 3.0.3 on 2020-05-17 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_track', '0004_sample'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='As_of',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Female_Dementia_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Female_Medicaid_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Female_Medicare_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Female_Private_Pay_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Male_Dementia_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Male_Medicaid_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Male_Medicare_Beds',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Open_Male_Private_Pay_Beds',
            field=models.IntegerField(),
        ),
    ]