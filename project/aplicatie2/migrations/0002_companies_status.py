# Generated by Django 4.2.7 on 2023-11-21 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicatie2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companies',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
