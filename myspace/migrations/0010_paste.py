# Generated by Django 3.2.12 on 2023-04-27 09:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myspace', '0009_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField(default=0)),
                ('title', models.TextField(default='', max_length=50)),
                ('author', models.TextField(blank=True, default='None', max_length=20)),
                ('content', models.TextField(default='', max_length=20000)),
                ('createtime', models.DateTimeField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['createtime'],
            },
        ),
    ]
