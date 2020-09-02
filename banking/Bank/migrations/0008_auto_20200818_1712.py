# Generated by Django 3.0.8 on 2020-08-18 11:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Bank', '0007_auto_20200817_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='name',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
