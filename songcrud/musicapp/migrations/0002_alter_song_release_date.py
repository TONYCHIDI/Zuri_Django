# Generated by Django 4.1.2 on 2022-11-04 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='release_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
