# Generated by Django 4.1 on 2022-08-28 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_rename_emai_users_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='user_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]