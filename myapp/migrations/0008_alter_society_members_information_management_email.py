# Generated by Django 3.2.9 on 2021-12-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_rename_familymember1_society_members_information_management_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='society_members_information_management',
            name='email',
            field=models.CharField(max_length=50),
        ),
    ]
