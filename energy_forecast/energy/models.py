from django.db import models


class EnergyBalance(models.Model):
    RESOURCE_CHOICES = [
        ('Электроэнергия', 'Электроэнергия'),
        ('Газ', 'Газ'),
        ('Нефть', 'Нефть'),
        ('Уголь', 'Уголь'),
        ('Теплоэнергия', 'Теплоэнергия'),
        ('Прочее', 'Прочее'),
        ('Ветер', 'Ветер'),
        ('Солнце', 'Солнце'),
        ('Торф', 'Торф'),
        ('Ядерная энергия', 'Ядерная энергия'),
    ]

    resource = models.CharField(max_length=100, choices=RESOURCE_CHOICES)
    year = models.IntegerField()
    city = models.CharField(max_length=100, null=True, blank=True)
    production = models.FloatField()
    import_value = models.FloatField()
    export_value = models.FloatField()
    price_per_unit = models.FloatField(null=True, blank=True)
    revenue = models.FloatField(null=True, blank=True)
    consumption = models.FloatField()
    generation_type = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        unique_together = ('resource', 'year', 'city')

    def __str__(self):
        return f"{self.resource} - {self.year} - {self.city}"
