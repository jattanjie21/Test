from django.db import models

# inventory table
class Inventory(models.Model):
    name          = models.CharField(max_length=100)
    quantity      = models.IntegerField()
    description   = models.TextField(blank=True,null=True)
    purchase_date = models.DateField()
    price         = models.DecimalField(max_digits=10, decimal_places=2)
    image         = models.ImageField(upload_to='inventory/',null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Inventories'