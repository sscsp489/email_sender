# Generated by Django 3.0.1 on 2020-05-18 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mail', '0003_auto_20200518_1906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='emails',
            name='owner',
        ),
    ]
