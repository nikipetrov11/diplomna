# Generated by Django 4.1.1 on 2022-09-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('cars', '0001_create_car_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_event', models.DateTimeField()),
                ('km_of_car', models.IntegerField()),
                ('event_text', models.TextField()),
                ('periodic_event', models.BooleanField()),
                ('next_date', models.DateField()),
                ('next_change', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='car',
            name='year_of_make',
            field=models.DateField(),
        ),
    ]