# Generated by Django 3.0.7 on 2020-06-17 07:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20200617_0746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='field',
            name='member',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field', to='members.Member'),
        ),
    ]
