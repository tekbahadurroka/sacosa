# Generated by Django 4.2.6 on 2023-10-10 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchsetup',
            name='branch_code',
            field=models.CharField(default=django.utils.timezone.now, max_length=10),
            preserve_default=False,
        ),
    ]
