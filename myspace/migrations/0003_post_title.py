# Generated by Django 3.2.12 on 2023-03-11 01:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0002_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.TextField(default='', max_length=50),
        ),
    ]
