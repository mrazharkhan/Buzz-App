# Generated by Django 5.1 on 2024-08-27 12:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buzz', '0006_alter_post_title_alter_like_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at'], 'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
    ]
