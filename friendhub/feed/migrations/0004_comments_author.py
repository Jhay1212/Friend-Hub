# Generated by Django 5.1.4 on 2025-01-19 02:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0003_chirp_engagement_comments'),
        ('users', '0002_follows_followers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='users.profile'),
        ),
    ]
