# Generated by Django 5.1 on 2024-08-27 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_customuser_phone_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'ordering': ['username'], 'verbose_name': 'user', 'verbose_name_plural': 'Users'},
        ),
    ]
