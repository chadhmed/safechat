# Generated by Django 5.0.1 on 2024-05-12 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_profile_ip'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='oldip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
