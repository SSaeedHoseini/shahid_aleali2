# Generated by Django 4.2.11 on 2024-03-06 18:24

from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0004_menuitem_deps_alter_menuitem_groups_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='deps',
        ),
        migrations.RemoveField(
            model_name='menuitem',
            name='order',
        ),
        migrations.AddField(
            model_name='menuitem',
            name='level',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='lft',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='rght',
            field=models.PositiveIntegerField(default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menuitem',
            name='tree_id',
            field=models.PositiveIntegerField(db_index=True, default=0, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='parent',
            field=mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='childrens', to='menu.menuitem'),
        ),
    ]
