# Generated by Django 3.1.7 on 2021-04-30 06:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ngoapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sinfo',
            name='Confirm',
        ),
        migrations.RemoveField(
            model_name='tinfo',
            name='Confirm',
        ),
    ]