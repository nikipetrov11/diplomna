# Generated by Django 4.2 on 2023-04-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cars', '0009_create_user_profile_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicerequest',
            name='is_seen',
            field=models.BooleanField(default=False),
        ),
    ]
