# Generated by Django 5.1.4 on 2024-12-24 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IrrigationZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('soil_moisture', models.FloatField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
    ]