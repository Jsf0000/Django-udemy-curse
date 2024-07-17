from django.db import models

class BookNumber(models.Model):
    id = models.BigAutoField(primary_key=True)
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=10, blank=True)

# Create your models here.
class Book(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=36, blank=False, unique=True, null=False)
    description = models.TextField(max_length=256, blank=True, default='')
    price = models.DecimalField(default=0, decimal_places=2, max_digits=10)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)
    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    # show the titles in admin section
    def __str__(self):
        return self.title

class Characters(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=20, blank=True)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='characters')

class Author(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    books = models.ManyToManyField(Book, related_name='authors')





