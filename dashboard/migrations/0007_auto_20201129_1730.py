# Generated by Django 3.0.7 on 2020-11-29 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20201129_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='latestupdate',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='latestupdate',
            old_name='var',
            new_name='Var',
        ),
    ]
