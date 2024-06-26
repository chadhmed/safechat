# Generated by Django 5.0.1 on 2024-05-05 03:03

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_groupchat_administrators_groupchat_owner'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupchat',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_group_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
