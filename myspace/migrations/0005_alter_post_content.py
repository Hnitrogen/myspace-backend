# Generated by Django 3.2.12 on 2023-03-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0004_hackerimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, default='', max_length=5000, null=True),
        ),
    ]
