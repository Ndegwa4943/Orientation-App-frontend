# Generated by Django 5.0.7 on 2024-07-25 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_alter_account_managers_alter_account_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='name',
        ),
        migrations.AlterField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]