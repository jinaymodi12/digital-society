# Generated by Django 3.2.9 on 2022-01-11 08:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('memberapp', '0003_rename_email_user_mail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='mail',
            new_name='email',
        ),
    ]
