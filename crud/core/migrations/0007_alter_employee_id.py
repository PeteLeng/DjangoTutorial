# Generated by Django 4.1.3 on 2022-11-21 07:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('3ac79c38-8bfb-4b6a-9e6c-40da8109d6a2'), editable=False, primary_key=True, serialize=False),
        ),
    ]
