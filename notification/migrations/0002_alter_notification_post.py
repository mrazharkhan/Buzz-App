# Generated by Django 5.1 on 2024-09-12 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buzz', '0010_post_comment_count_post_like_count_post_view_count'),
        ('notification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notifications', to='buzz.post'),
        ),
    ]
