# Generated by Django 5.0.6 on 2024-07-15 12:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0002_alter_student_options_alter_student_teacher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'verbose_name': 'Ученик', 'verbose_name_plural': 'Ученики'},
        ),
    ]
