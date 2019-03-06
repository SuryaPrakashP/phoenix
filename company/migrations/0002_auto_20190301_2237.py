# Generated by Django 2.0.4 on 2019-03-01 17:07

from django.db import migrations, models
import phonenumber_field.modelfields


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
        migrations.RemoveField(
            model_name='email',
            name='attach',
        ),
        migrations.AddField(
            model_name='email',
            name='resume',
            field=models.FileField(default=0, upload_to='img/'),
        ),
        migrations.AlterField(
            model_name='email',
            name='Phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128),
        ),
    ]