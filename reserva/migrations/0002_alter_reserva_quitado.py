# Generated by Django 4.2.5 on 2023-09-07 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserva', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='quitado',
            field=models.CharField(max_length=3),
        ),
    ]