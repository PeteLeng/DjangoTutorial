# Generated by Django 4.1.3 on 2022-11-21 03:36

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('6f1dda0d-c501-496f-96e0-5dec98da2220'), editable=False, primary_key=True, serialize=False),
        ),
    ]
