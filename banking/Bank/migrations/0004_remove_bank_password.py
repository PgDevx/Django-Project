# Generated by Django 3.0.8 on 2020-08-16 18:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Bank', '0003_auto_20200815_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bank',
            name='password',
        ),
    ]
