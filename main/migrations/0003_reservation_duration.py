# Generated by Django 5.1.3 on 2024-12-05 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_guest_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='duration',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]