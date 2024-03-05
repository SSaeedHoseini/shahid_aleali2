# Generated by Django 4.2.8 on 2023-12-28 08:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("schools", "0002_alter_parent_person_alter_student_person_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="academicyear",
            options={"verbose_name": "academic year", "verbose_name_plural": "academic years"},
        ),
        migrations.AlterModelOptions(
            name="attendance",
            options={"verbose_name": "attendance", "verbose_name_plural": "attendances"},
        ),
        migrations.AlterModelOptions(
            name="class",
            options={"verbose_name": "class", "verbose_name_plural": "Classes"},
        ),
        migrations.AlterModelOptions(
            name="classschedule",
            options={"verbose_name": "class schedule", "verbose_name_plural": "classe schedules"},
        ),
        migrations.AlterModelOptions(
            name="exam",
            options={"verbose_name": "exam", "verbose_name_plural": "exams"},
        ),
        migrations.AlterModelOptions(
            name="examscore",
            options={"verbose_name": "exam score", "verbose_name_plural": "exam scores"},
        ),
        migrations.AlterModelOptions(
            name="gradelevel",
            options={"verbose_name": "grade level", "verbose_name_plural": "grade levels"},
        ),
        migrations.AlterModelOptions(
            name="lesson",
            options={"verbose_name": "lesson", "verbose_name_plural": "lessons"},
        ),
        migrations.AlterModelOptions(
            name="parent",
            options={"verbose_name": "parent", "verbose_name_plural": "parents"},
        ),
        migrations.AlterModelOptions(
            name="school",
            options={"verbose_name": "school", "verbose_name_plural": "schools"},
        ),
        migrations.AlterModelOptions(
            name="student",
            options={"verbose_name": "student", "verbose_name_plural": "students"},
        ),
        migrations.AlterModelOptions(
            name="subject",
            options={"verbose_name": "subject", "verbose_name_plural": "subjects"},
        ),
        migrations.AlterModelOptions(
            name="teacher",
            options={"verbose_name": "teacher", "verbose_name_plural": "teachers"},
        ),
        migrations.AlterModelOptions(
            name="teachersubject",
            options={"verbose_name": "teacher subject", "verbose_name_plural": "teacher subjects"},
        ),
    ]
