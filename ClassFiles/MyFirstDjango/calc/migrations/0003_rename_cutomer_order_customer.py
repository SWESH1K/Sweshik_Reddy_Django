# Generated by Django 5.0.7 on 2024-07-27 05:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='cutomer',
            new_name='customer',
        ),
    ]
