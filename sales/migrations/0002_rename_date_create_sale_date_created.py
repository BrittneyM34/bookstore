# Generated by Django 4.2.14 on 2024-08-15 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='date_create',
            new_name='date_created',
        ),
    ]
