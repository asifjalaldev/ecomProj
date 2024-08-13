from django.db import models


class ProductImage(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(
                upload_to='product_images',
                null=True, blank=True
                )
    
    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    name = models.CharField(max_length=50)


class ProductBrand(models.Model):
    name = models.CharField(max_length=50)
      
    def __str__(self):
        return self.name


class CategoryAttributes(models.Model):
    category = models.ForeignKey(
            ProductCategory,
            on_delete=models.CASCADE, 
            null=True, blank=True
            )
    
    attribute_name = models.CharField(max_length=150)
    attribute_value = models.CharField(max_length=150)

    def __str__(self):
        return self.category.name


class Product(models.Model):
    product_images = models.ForeignKey(
        ProductImage, 
        on_delete=models.CASCADE, 
        null=True, blank=True
        )

    product_category = models.ForeignKey(
        ProductCategory,
        on_delete=models.CASCADE,
        null=True, blank=True
        )
    
    product_brand = models.ForeignKey(
        ProductBrand, 
        on_delete=models.CASCADE, 
        null=True, blank=True
        )
    
    name = models.CharField(max_length=150)
    price = models.DecimalField(decimal_places=2)
    description = models.TextField()
      
    def __str__(self):
        return self.name