from django.contrib import admin
from products.models import Product, ProductBrand, ProductCategory, ProductImage
# Register your models here.

admin.site.register(Product)
admin.site.register(ProductCategory)
admin.site.register(ProductBrand)
admin.site.register(ProductImage)
