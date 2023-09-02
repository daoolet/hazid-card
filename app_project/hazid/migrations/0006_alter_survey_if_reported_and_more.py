# Generated by Django 4.2.4 on 2023-09-02 05:40

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('hazid', '0005_alter_survey_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='survey',
            name='if_reported',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='survey',
            name='possible_consequences',
            field=multiselectfield.db.fields.MultiSelectField(choices=[('Injury/Illness', 'Injury/Illness'), ('Environmental damage/spill', 'Environmental damage/spill'), ('Equipment/property damage/loss', 'Equipment/property damage/loss'), ('Fire', 'Fire'), ('Motor vehicle accident', 'Motor vehicle accident'), ('Other', 'Other')], max_length=255),
        ),
    ]
