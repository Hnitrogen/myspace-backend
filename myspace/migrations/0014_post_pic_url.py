# Generated by Django 3.2.12 on 2023-05-30 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0013_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic_url',
            field=models.TextField(default='https://www.colopen-blog.com/image/images/2023/04/08/003.jpg', max_length=50),
        ),
    ]
