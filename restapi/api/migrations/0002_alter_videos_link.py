# Generated by Django 4.2.1 on 2024-02-23 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='videos',
            name='link',
            field=models.URLField(max_length=100),
        ),
    ]
