# Generated by Django 2.2 on 2022-03-23 05:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_auto_20220322_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='class',
            old_name='school_obj',
            new_name='school_id',
        ),
    ]
