from django.contrib import admin
from .models import Category, Brand, Size, Color, Product, Subcategory
# Category
admin.site.register(Category)
# SubCategory
admin.site.register(Subcategory)
#brand
admin.site.register(Brand)
#Color
admin.site.register(Color)
#Size
admin.site.register(Size)
#Product
@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','brand','category','sub_category','selling_price','discounted_price']
