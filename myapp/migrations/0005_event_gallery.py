# Generated by Django 3.2.9 on 2021-12-22 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_society_problem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event_gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('disc', models.CharField(max_length=50)),
                ('pics', models.FileField(blank=True, null=True, upload_to='profile')),
            ],
        ),
    ]
