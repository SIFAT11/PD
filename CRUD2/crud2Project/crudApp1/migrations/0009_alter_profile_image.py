# Generated by Django 4.1.7 on 2023-03-11 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crudApp1', '0008_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Image',
            field=models.ImageField(blank=True, default='default/default.jpg', null=True, upload_to='prof_pic/'),
        ),
    ]
