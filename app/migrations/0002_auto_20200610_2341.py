# Generated by Django 3.0.6 on 2020-06-10 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Capita',
            new_name='Capital',
        ),
        migrations.RenameField(
            model_name='capital',
            old_name='capitaranges',
            new_name='capita_ranges',
        ),
    ]
