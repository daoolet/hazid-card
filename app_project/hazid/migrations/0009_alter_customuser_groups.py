# Generated by Django 4.2.4 on 2023-09-10 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('hazid', '0008_alter_customuser_options_alter_survey_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='groups',
            field=models.ManyToManyField(blank=True, to='auth.group'),
        ),
    ]
