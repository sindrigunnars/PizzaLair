# Generated by Django 4.0.4 on 2023-05-02 20:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0003_alter_pizza_type'),
        ('offers', '0007_remove_offeritems_item_count_offeritems_count'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='offeritems',
            name='count',
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='menu.pizza')),
            ],
        ),
        migrations.AlterField(
            model_name='offeritems',
            name='items',
            field=models.ManyToManyField(to='offers.item'),
        ),
    ]
