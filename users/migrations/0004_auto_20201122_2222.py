# Generated by Django 3.1.1 on 2020-11-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201122_2213'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='phone_number',
        ),
    ]
