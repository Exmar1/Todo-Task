# Generated by Django 5.1.5 on 2025-02-08 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskitem',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
