from unicodedata import category
from django.db import models
from numpy import product
from products.models import Category, Product
# Static-Pages.
class StaticPosts(models.Model):
    title = models.CharField(max_length=160)
    page_name = models.CharField(max_length=70)
    content = models.TextField()
    slug = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.title


# Site-Data.
class SiteData(models.Model):
    email = models.CharField(max_length=160, default="")
    phone =models.IntegerField(default=123456789)
    facebook = models.CharField(max_length=160,  default="", blank=True, null=True)
    instagram = models.CharField(max_length=160,  default="", blank=True, null=True)
    twitter = models.CharField(max_length=160,default="", blank=True, null=True)
    youtube = models.CharField(max_length=160,default="", blank=True, null=True)
    address = models.CharField(max_length=260,default="")
    made_by = models.CharField(max_length=160,default="")
    copyright = models.CharField(max_length=160,default="")


#==Home-Section-1==================#
class HomeSectionOne(models.Model):
    section_title = models.CharField(max_length=160)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.section_title