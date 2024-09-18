
from django.db import models
from django.urls import reverse


class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )

    class Meta:
        db_table = "category"
        verbose_name = "Категорию"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name="Название")
    slug = models.SlugField(
        max_length=200, unique=True, blank=True, null=True, verbose_name="URL"
    )
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="goods_images", blank=True, null=True)
    image2 = models.ImageField(upload_to="goods_images", blank=True, null=True)
    image3 = models.ImageField(upload_to="goods_images", blank=True, null=True)
    image4 = models.ImageField(upload_to="goods_images", blank=True, null=True)
    image5 = models.ImageField(upload_to="goods_images", blank=True, null=True)
    image6 = models.ImageField(upload_to="goods_images", blank=True, null=True)
    price = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, blank=True, null=True
    )
    discount = models.DecimalField(
        default=0.00, max_digits=7, decimal_places=2, blank=True, null=True
    )
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE)

    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("id",)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("catalog:product", kwargs={"product_slug": self.slug})
    

    def display_id(self):
        return f"{self.id:05}"
    
    def sell_price(self):
        if self.discount:
            return round(self.price - self.price * self.discount/100,2)
        
        return self.price
