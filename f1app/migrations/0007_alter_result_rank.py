# Generated by Django 4.1.1 on 2022-10-05 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f1app", "0006_rename_result_constructor_result_constructor_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="result",
            name="rank",
            field=models.PositiveIntegerField(null=True),
        ),
    ]