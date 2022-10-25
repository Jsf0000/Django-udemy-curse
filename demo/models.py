from django.db import models


# Create your models here.
class Book(models.Model):
    # STATUSES = (
    #     (0, 'Unknown'),
    #     (1, 'processed'),
    #     (2, 'paid')
    # )
    title = models.CharField(max_length=36, blank=False, unique=True)
    description = models.TextField(max_length=256, blank=True, default='')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)



