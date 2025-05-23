# Generated by Django 5.2 on 2025-05-08 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('energy', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='energybalance',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='energybalance',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='energybalance',
            name='generation_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='energybalance',
            name='price_per_unit',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='energybalance',
            name='revenue',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='energybalance',
            name='resource',
            field=models.CharField(choices=[('Электроэнергия', 'Электроэнергия'), ('Газ', 'Газ'), ('Нефть', 'Нефть'), ('Уголь', 'Уголь'), ('Теплоэнергия', 'Теплоэнергия'), ('Прочее', 'Прочее'), ('Ветер', 'Ветер'), ('Солнце', 'Солнце'), ('Торф', 'Торф'), ('Ядерная энергия', 'Ядерная энергия')], max_length=100),
        ),
        migrations.AlterUniqueTogether(
            name='energybalance',
            unique_together={('resource', 'year', 'city')},
        ),
    ]
