# Generated by Django 3.1.7 on 2021-07-01 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_remove_about_favicon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='background',
        ),
    ]