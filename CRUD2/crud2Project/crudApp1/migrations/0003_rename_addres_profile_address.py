# Generated by Django 4.1.7 on 2023-02-25 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp1', '0002_alter_profile_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='Addres',
            new_name='Address',
        ),
    ]
