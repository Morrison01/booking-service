from django.db import models

class ImportedProduct(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    origin_country = models.CharField(max_length=100, verbose_name="Країна походження")
    import_date = models.DateField(verbose_name="Дата імпорту")
    description = models.TextField(blank=True, null=True, verbose_name="Опис товару")

    def __str__(self):
        return self.name
