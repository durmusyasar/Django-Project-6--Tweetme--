# Generated by Django 2.2.4 on 2019-08-23 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_auto_20190821_1440'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tweet',
            options={'ordering': ['timestamp']},
        ),
    ]
