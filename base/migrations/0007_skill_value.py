# Generated by Django 3.1.7 on 2021-06-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_about_freelance'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='value',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
