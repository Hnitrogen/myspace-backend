# Generated by Django 3.2.12 on 2023-04-24 12:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0008_todolist'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.TextField(default='', max_length=50)),
                ('brief', models.TextField(default='', max_length=50)),
                ('goto_url', models.TextField(default='', max_length=200)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['createtime'],
            },
        ),
    ]
