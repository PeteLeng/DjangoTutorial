# Generated by Django 4.1.3 on 2022-11-21 08:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_alter_employee_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='id',
            field=models.UUIDField(default=uuid.UUID('71762415-6933-4f34-a2b9-dc67d883e69a'), editable=False, primary_key=True, serialize=False),
        ),
    ]
