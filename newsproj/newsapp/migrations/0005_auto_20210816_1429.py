# Generated by Django 3.1.5 on 2021-08-16 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsapp', '0004_auto_20210815_1759'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='author',
        ),
        migrations.AddField(
            model_name='articles',
            name='author',
            field=models.ManyToManyField(to='newsapp.Authors'),
        ),
    ]
