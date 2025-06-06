# Generated by Django 5.2 on 2025-05-05 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EnergyBalance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resource', models.CharField(choices=[('Электроэнергия', 'Электроэнергия'), ('Газ', 'Газ'), ('Нефть', 'Нефть'), ('Уголь', 'Уголь'), ('Теплоэнергия', 'Теплоэнергия'), ('Прочее', 'Прочее')], max_length=100)),
                ('year', models.IntegerField()),
                ('production', models.FloatField()),
                ('import_value', models.FloatField()),
                ('export_value', models.FloatField()),
                ('consumption', models.FloatField()),
            ],
            options={
                'unique_together': {('resource', 'year')},
            },
        ),
    ]
