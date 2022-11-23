# Generated by Django 4.1.3 on 2022-11-17 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("membership_tiers", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="membership",
            name="membership_type",
            field=models.CharField(
                choices=[
                    ("Enterprise", "Enterprise"),
                    ("Premium", "Premium"),
                    ("Basic", "Basic"),
                ],
                default="Basic",
                max_length=30,
            ),
        ),
    ]
