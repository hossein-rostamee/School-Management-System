# Generated by Django 4.2.3 on 2023-10-04 13:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_student_whichbooksdoyouliketoread_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='date',
            field=models.DateField(db_column='anvar_date', default='2018-11-20'),
        ),
        migrations.AddField(
            model_name='volunteer',
            name='date',
            field=models.DateField(db_column='anvar_date', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
