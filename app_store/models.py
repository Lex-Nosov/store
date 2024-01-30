from django.db import models


class Category(models.Model):
    name_category = models.TextField(max_length=50)
    name_category_ru = models.TextField(max_length=50, blank=True)
    url = models.SlugField(max_length=100, default=name_category)

    def __str__(self):
        return self.name_category_ru


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_length=10, decimal_places=2, max_digits=10)
    discount = models.PositiveIntegerField()
    description_for_cart = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='static/img/', blank=True)
    stock = models.PositiveIntegerField(default=0, )
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    archived = models.BooleanField(default=False)
    category_field = models.ForeignKey(Category, related_name='products', on_delete=models.PROTECT)

    def get_absolute_url(self):
        return '/products/'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'products'
        verbose_name_plural = 'products'
        ordering = ['name']


class Characteristics(models.Model):
    article = models.TextField(max_length=100, blank=True)
    country_manufacture = models.TextField(max_length=100, blank=True)
    product_life = models.TextField(max_length=100, blank=True)
    warranty_period = models.TextField(max_length=100, blank=True)
    operating_system = models.TextField(max_length=100, blank=True)
    case_material = models.TextField(max_length=100, blank=True)
    weight = models.TextField(max_length=100, blank=True)
    dimensions = models.TextField(max_length=100, blank=True)
    processor = models.TextField(max_length=100, blank=True)
    number_processor_cores = models.TextField(max_length=100, blank=True)
    ram = models.TextField(max_length=100, blank=True)
    integrated = models.TextField(max_length=100, blank=True)
    internal_memory = models.TextField(max_length=100, blank=True)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.article


class Overview(models.Model):
    first_title = models.TextField(max_length=50, blank=True)
    first_description = models.TextField(max_length=1000, blank=True)
    second_title = models.TextField(max_length=50, blank=True)
    second_description = models.TextField(max_length=1000, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.first_title
