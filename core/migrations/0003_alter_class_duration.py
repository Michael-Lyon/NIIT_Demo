# Generated by Django 4.1.7 on 2023-05-22 13:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0002_class_teacher"),
    ]

    operations = [
        migrations.AlterField(
            model_name="class",
            name="duration",
            field=models.CharField(max_length=100),
        ),
    ]
