# Generated by Django 3.0.7 on 2020-06-16 05:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('publications', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='caption',
        ),
        migrations.AlterField(
            model_name='link',
            name='publication',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='publication', to='publications.Publication'),
        ),
    ]
