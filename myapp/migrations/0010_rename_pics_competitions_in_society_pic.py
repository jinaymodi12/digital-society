# Generated by Django 3.2.9 on 2021-12-27 06:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_competitions_in_society'),
    ]

    operations = [
        migrations.RenameField(
            model_name='competitions_in_society',
            old_name='pics',
            new_name='pic',
        ),
    ]