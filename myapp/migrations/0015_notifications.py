# Generated by Django 3.2.9 on 2022-01-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0014_rename_pics_competitions_in_society_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='notifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('disc', models.TextField(max_length=50)),
            ],
        ),
    ]
