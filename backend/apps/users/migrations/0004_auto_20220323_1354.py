# Generated by Django 2.2 on 2022-03-23 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
        ('users', '0003_auto_20220322_2120'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='school_obj',
            new_name='school_id',
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together={('username', 'school_id')},
        ),
    ]
