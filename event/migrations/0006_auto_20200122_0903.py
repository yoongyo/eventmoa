# Generated by Django 2.1 on 2020-01-22 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0005_auto_20200121_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='partner',
            old_name='image',
            new_name='logo',
        ),
    ]
