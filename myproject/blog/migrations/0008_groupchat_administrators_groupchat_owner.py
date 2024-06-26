# Generated by Django 5.0.1 on 2024-05-05 03:02

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_groupmessage_group_chat'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='groupchat',
            name='administrators',
            field=models.ManyToManyField(related_name='administered_group_chats', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='groupchat',
            name='owner',
            field=models.ForeignKey(default='2', on_delete=django.db.models.deletion.CASCADE, related_name='owned_group_chats', to=settings.AUTH_USER_MODEL),
        ),
    ]
