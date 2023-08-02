# Generated by Django 4.2 on 2023-07-27 13:21

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Appointment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Phone number must not contain spaces, letters, parentheses or dashes. It must contain 10 digits.",
                        max_length=10,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Phone number must not contain spaces, letters, parentheses or dashes. It must contain 10 digits.",
                                regex="^\\d{10}$",
                            )
                        ],
                    ),
                ),
                (
                    "address",
                    models.CharField(
                        blank=True,
                        default="",
                        help_text="Does not have to be specific, just the city and the state",
                        max_length=255,
                        null=True,
                    ),
                ),
                ("want_reminder", models.BooleanField(default=False)),
                ("additional_info", models.TextField(blank=True, null=True)),
                ("paid", models.BooleanField(default=False)),
                (
                    "amount_to_pay",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=6, null=True
                    ),
                ),
                ("id_request", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Config",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "slot_duration",
                    models.PositiveIntegerField(
                        help_text="Minimum time for an appointment in minutes, recommended 30.",
                        null=True,
                    ),
                ),
                (
                    "lead_time",
                    models.TimeField(
                        help_text="Time when we start working.", null=True
                    ),
                ),
                (
                    "finish_time",
                    models.TimeField(help_text="Time when we stop working.", null=True),
                ),
                (
                    "appointment_buffer_time",
                    models.FloatField(
                        help_text="Time between now and the first available slot for the current day (doesn't affect tomorrow).",
                        null=True,
                    ),
                ),
                (
                    "website_name",
                    models.CharField(
                        default="", help_text="Name of your website.", max_length=255
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Service",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("duration", models.DurationField()),
                ("price", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "down_payment",
                    models.DecimalField(decimal_places=2, default=0, max_digits=6),
                ),
                ("currency", models.CharField(default="USD", max_length=3)),
                (
                    "image",
                    models.ImageField(blank=True, null=True, upload_to="services/"),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="PaymentInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "appointment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointment.appointment",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="EmailVerificationCode",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("code", models.CharField(max_length=6)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="AppointmentRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("start_time", models.TimeField()),
                ("end_time", models.TimeField()),
                (
                    "payment_type",
                    models.CharField(
                        choices=[("full", "Full payment"), ("down", "Down payment")],
                        default="full",
                        max_length=4,
                    ),
                ),
                ("id_request", models.CharField(blank=True, max_length=100, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "service",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="appointment.service",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="appointment",
            name="appointment_request",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="appointment.appointmentrequest",
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="client",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
