# Generated by Django 3.2.5 on 2021-07-20 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_variation'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='variation',
            options={'verbose_name': 'Variação', 'verbose_name_plural': 'Variações'},
        ),
    ]
