# Generated by Django 3.0.3 on 2020-11-10 15:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20201109_1414'),
    ]

    operations = [
        migrations.AddField(
            model_name='queries',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]