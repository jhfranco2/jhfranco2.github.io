# Generated by Django 4.1.7 on 2023-03-30 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0002_rename_description_libro_descripccion'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='descripccion',
            new_name='descripcion',
        ),
    ]
