# Generated by Django 4.1.7 on 2023-03-28 15:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("tracker", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="redactor",
            name="years_of_experience",
            field=models.IntegerField(null=True),
        ),
    ]