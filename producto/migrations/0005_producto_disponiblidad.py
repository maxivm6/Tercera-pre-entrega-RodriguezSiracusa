# Generated by Django 4.1.4 on 2023-01-12 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0004_remove_producto_disponibilidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='disponiblidad',
            field=models.BooleanField(default=1),
            preserve_default=False,
        ),
    ]
