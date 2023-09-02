from django.db import models

# Category
class Category(models.Model):
    name = models.CharField(max_length=160, unique= True)
    category_img = models.ImageField(upload_to = 'category_img', null = True, blank = True)
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Category.objects.get(id=self.id)
            if this.category_img != self.category_img:
                this.category_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Category, self).save(*args, **kwargs)

# SubCategory
class Subcategory(models.Model):
    name = models.CharField(max_length=160, unique= True)
    
    def __str__(self):
        return self.name

# Brand
class Brand(models.Model):
    name = models.CharField(max_length=160, unique= True)
    
    def __str__(self):
        return self.name
#color
class Color(models.Model):
    name = models.CharField(max_length=160, unique= True)
    color_img = models.ImageField(upload_to='color_img')
    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Color.objects.get(id=self.id)
            if this.color_img != self.color_img:
                this.color_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Color, self).save(*args, **kwargs)

#size
class Size(models.Model):
    name = models.CharField(max_length=160, unique= True)
    
    def __str__(self):
        return self.name

# Product
class Product(models.Model):
    title = models.CharField(max_length=160)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    selling_price = models.FloatField()
    discounted_price = models.FloatField()
    shipping_price = models.FloatField(default=0)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE)
    product_img = models.ImageField(upload_to='product_img')
    ingredients = models.CharField(max_length=300)
    how_use = models.CharField(max_length=500)
    pro_tips = models.CharField(max_length=500)
    ingredients = models.CharField(max_length=300)
    heighlights = models.TextField(default='''
    <strong>What is it? </strong>
    <p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Reiciendis vero voluptas ducimus inventore enim. Voluptas ipsam modi aliquid dicta voluptatem sit rem praesentium repellat corrupti, officia ducimus quos saepe molestias.</p>
    <br/>
    <strong>What makes it special? </strong>
    <ul>
        <li>Olive Oil Glossing Polish (6oz) enhances your hair for incredible shine and restores moisture to hair </li>
        <li>Helps to eliminate frizz and fly-always and resist humidity for longer lasting style </li>
        <li>Helps to leave hair healthy and more manageable </li>
    </ul>''')
    color = models.ManyToManyField(Color, blank=True)
    size = models.ManyToManyField(Size, blank=True)
    permalink =models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = Product.objects.get(id=self.id)
            if this.product_img != self.product_img:
                this.product_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(Product, self).save(*args, **kwargs)




    
