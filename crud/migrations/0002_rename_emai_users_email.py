# Generated by Django 4.1 on 2022-08-24 02:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='emai',
            new_name='email',
        ),
    ]