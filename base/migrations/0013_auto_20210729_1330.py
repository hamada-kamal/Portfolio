# Generated by Django 3.1.7 on 2021-07-29 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_about_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='whatsapp_link',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]