# Generated by Django 2.2.5 on 2021-07-15 10:29

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_bookedday'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookedday',
            options={'verbose_name': 'Booked Day', 'verbose_name_plural': 'Booked Days'},
        ),
        migrations.AddField(
            model_name='bookedday',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookedday',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
