from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    state = models.CharField(max_length=100, default="None")
    address = models.CharField(max_length=200, default="None")
    city = models.CharField(max_length=100, default="None")
    zip_code = models.IntegerField(default="123")
    email = models.EmailField(unique=True)
    phone = models.IntegerField(default = 123456789)
    profile_img = models.ImageField(default = 'static/images/account/default_profile.png', upload_to = 'profile_img', null = True, blank = True)

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # delete old file when replacing by updating the file
        try:
            this = User.objects.get(id=self.id)
            if this.profile_img != self.profile_img:
                this.profile_img.delete(save=False)
        except: pass # when new photo then we do nothing, normal case          
        super(User, self).save(*args, **kwargs)


class Customer(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=100)
    zip_code = models.IntegerField()

    def __str__(self):
        return str(self.id)