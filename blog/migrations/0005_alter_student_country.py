# Generated by Django 4.1.3 on 2022-11-28 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0004_student_country_student_gender_student_image_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="country",
            field=models.CharField(
                choices=[("nepal", "Nepal"), ("india", "India"), ("china", "China")],
                max_length=100,
                null=True,
            ),
        ),
    ]
