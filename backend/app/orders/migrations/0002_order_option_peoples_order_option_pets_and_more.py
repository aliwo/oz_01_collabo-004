# Generated by Django 5.0.4 on 2024-04-05 07:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("orders", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="option_peoples",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="option_pets",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="pet_size_big",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="pet_size_medium",
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name="order",
            name="pet_size_small",
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="order",
            name="status",
            field=models.CharField(
                choices=[("CANCEL", "cancel"), ("PAID", "paid"), ("ORDERED", "ordered")], max_length=7
            ),
        ),
    ]