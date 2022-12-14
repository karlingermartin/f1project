# Generated by Django 4.1.1 on 2022-10-05 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("f1app", "0004_rename_circuit_id_races_circuit"),
    ]

    operations = [
        migrations.RenameField(
            model_name="result",
            old_name="result_constructor_id",
            new_name="result_constructor",
        ),
        migrations.RenameField(
            model_name="result",
            old_name="result_driver_id",
            new_name="result_driver",
        ),
        migrations.RenameField(
            model_name="result",
            old_name="result_race_id",
            new_name="result_race",
        ),
        migrations.RemoveField(
            model_name="circuit",
            name="circuit_id",
        ),
        migrations.RemoveField(
            model_name="constructor",
            name="constructor_id",
        ),
        migrations.RemoveField(
            model_name="driver",
            name="driver_id",
        ),
        migrations.RemoveField(
            model_name="races",
            name="race_id",
        ),
        migrations.RemoveField(
            model_name="result",
            name="result_id",
        ),
        migrations.AddField(
            model_name="circuit",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="constructor",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="driver",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="races",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="result",
            name="id",
            field=models.BigAutoField(
                auto_created=True,
                default=None,
                primary_key=True,
                serialize=False,
                verbose_name="ID",
            ),
            preserve_default=False,
        ),
    ]
