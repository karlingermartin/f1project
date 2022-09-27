# Generated by Django 4.1 on 2022-09-27 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Circuit",
            fields=[
                (
                    "circuit_id",
                    models.AutoField(default="0", primary_key=True, serialize=False),
                ),
                ("circuit_name", models.CharField(max_length=100)),
                ("circuit_city", models.CharField(max_length=100)),
                ("circuit_country", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Constructor",
            fields=[
                (
                    "constructor_id",
                    models.AutoField(default="0", primary_key=True, serialize=False),
                ),
                ("constructor_name", models.CharField(max_length=100, unique=True)),
                ("constructor_nationality", models.CharField(max_length=100)),
                (
                    "constructor_race_wins",
                    models.PositiveIntegerField(verbose_name="auth.User"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Driver",
            fields=[
                (
                    "driver_id",
                    models.AutoField(default="0", primary_key=True, serialize=False),
                ),
                ("forename", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                ("driver_nationality", models.CharField(max_length=100)),
                ("race_wins", models.PositiveIntegerField(verbose_name="auth.User")),
                (
                    "championships",
                    models.PositiveIntegerField(verbose_name="auth.User"),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Races",
            fields=[
                (
                    "race_id",
                    models.AutoField(default="0", primary_key=True, serialize=False),
                ),
                ("race_year", models.PositiveIntegerField()),
                ("round", models.PositiveIntegerField()),
                ("race_name", models.CharField(max_length=100)),
                ("date", models.DateField()),
                (
                    "circuit_id_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="races",
                        to="f1app.circuit",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Result",
            fields=[
                (
                    "result_id",
                    models.AutoField(default="0", primary_key=True, serialize=False),
                ),
                ("grid", models.PositiveIntegerField()),
                ("position_order", models.PositiveIntegerField()),
                ("points", models.PositiveIntegerField()),
                ("laps", models.PositiveIntegerField()),
                ("rank", models.PositiveIntegerField()),
                (
                    "constructor_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="f1app.constructor",
                    ),
                ),
                (
                    "driver_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="f1app.driver",
                    ),
                ),
                (
                    "race_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="results",
                        to="f1app.races",
                    ),
                ),
            ],
        ),
    ]