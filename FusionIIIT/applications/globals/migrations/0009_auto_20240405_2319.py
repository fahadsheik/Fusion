# Generated by Django 3.1.5 on 2024-04-05 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('globals', '0008_auto_20240405_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extrainfo',
            name='user_status',
            field=models.CharField(choices=[('PRESENT', 'PRESENT'), ('NEW', 'NEW')], default='PRESENT', max_length=50),
        ),
    ]
