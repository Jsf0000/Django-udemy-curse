from django.db import models


# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=36, blank=False, unique=True, null=False)
    description = models.TextField(max_length=256, blank=True, default='')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    # show the titles in admin section
    def __str__(self):
        return self.title

