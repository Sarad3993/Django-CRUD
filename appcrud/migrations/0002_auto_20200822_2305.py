# Generated by Django 3.1 on 2020-08-22 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='contact',
            new_name='first_name',
        ),
        migrations.RemoveField(
            model_name='students',
            name='address',
        ),
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
        migrations.AddField(
            model_name='students',
            name='last_name',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]