# Generated by Django 3.2.12 on 2024-05-22 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='Todo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='main.todo'),
        ),
    ]
