# Generated by Django 4.2.6 on 2023-10-29 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator_app', '0002_branchsetup_branch_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchsetup',
            name='branch_code',
            field=models.IntegerField(null=True),
        ),
    ]
