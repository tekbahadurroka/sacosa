# Generated by Django 4.2.6 on 2023-10-29 09:04

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('adminstrator_app', '0005_alter_branchsetup_branch_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branchsetup',
            name='branch_code',
            field=models.IntegerField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
