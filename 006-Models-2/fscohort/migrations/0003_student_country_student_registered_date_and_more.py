# Generated by Django 4.1 on 2022-08-22 19:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("fscohort", "0002_alter_student_options_student_about_student_avatar"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="country",
            field=models.CharField(
                choices=[
                    ("TR", "TURKEY"),
                    ("US", "UNITED STATES"),
                    ("DE", "GERMANY"),
                    ("FR", "FRANCE"),
                ],
                default="TR",
                max_length=2,
                verbose_name="Country",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="registered_date",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="student",
            name="update_date",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
