# Generated by Django 3.2.6 on 2021-08-17 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tunr', '0002_auto_20210817_1744'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.CharField(default='no album title', max_length=100),
        ),
        migrations.AddField(
            model_name='song',
            name='preview_url',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='song',
            name='title',
            field=models.CharField(default='no song title', max_length=100),
        ),
    ]