# Generated by Django 2.0.4 on 2019-02-25 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_auto_20190225_2336'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='email',
            name='attach',
        ),
    ]
