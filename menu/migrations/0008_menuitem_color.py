# Generated by Django 4.2.11 on 2024-03-06 22:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0007_alter_menuitem_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='color',
            field=colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=25, samples=None),
        ),
    ]
