# Generated by Django 3.2.9 on 2021-11-14 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='age',
            field=models.IntegerField(max_length=6),
        ),
    ]
