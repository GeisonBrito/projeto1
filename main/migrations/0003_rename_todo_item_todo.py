# Generated by Django 5.0.4 on 2024-06-06 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("main", "0002_alter_item_todo"),
    ]

    operations = [
        migrations.RenameField(
            model_name="item",
            old_name="Todo",
            new_name="todo",
        ),
    ]
