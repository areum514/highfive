# Generated by Django 3.0.6 on 2020-06-08 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('equipments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='equiptment',
            name='created',
        ),
        migrations.RemoveField(
            model_name='equiptment',
            name='updated',
        ),
    ]
