# Generated by Django 3.1.1 on 2020-10-19 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='job_name',
            field=models.CharField(max_length=200),
        ),
    ]