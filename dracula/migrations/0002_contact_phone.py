# Generated by Django 3.2.3 on 2021-07-06 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dracula', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default='', max_length=20),
        ),
    ]
