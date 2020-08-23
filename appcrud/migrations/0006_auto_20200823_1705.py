# Generated by Django 3.1 on 2020-08-23 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appcrud', '0005_auto_20200823_1700'),
    ]

    operations = [
        migrations.RenameField(
            model_name='students',
            old_name='first_name',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='students',
            old_name='last_name',
            new_name='name',
        ),
        migrations.AddField(
            model_name='students',
            name='contact',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='students',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]