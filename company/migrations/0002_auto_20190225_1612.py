# Generated by Django 2.0.4 on 2019-02-25 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='email',
            old_name='Location',
            new_name='College_name',
        ),
        migrations.AlterField(
            model_name='email',
            name='attach',
            field=models.FileField(upload_to='media'),
        ),
    ]
