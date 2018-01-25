from django.db import models
import random
import os
from django.db.models import Q
from django.db.models.signals import pre_save,post_save
from .utils import unique_slug_generator
def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name,ext = os.path.splitext(base_name)
    return name, ext

def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,75435643456)
    name, ext = get_filename_ext(filename)
    final_filename = '{0}{1}'.format(new_filename,ext)
    return f"products/{new_filename}/{final_filename}"



# Create your models here.
class ProductQuerySet(models.query.QuerySet):
    def featured(self):
        return self.filter(featured=True)
    def searched(self,query):
        #return self.filter(title__icontains=query)
        lookups = Q(title__icontains=query) | Q(description__icontains=query)
        return self.filter(lookups).distinct()

class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model,using=self._db)
    def featured(self):
        return self.get_queryset().featured()
    def searched(self,query):
        return self.get_queryset().searched(query)


class product(models.Model):
    title = models.CharField(max_length=20)
    slug = models.SlugField(default='abc', blank=True, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=20,default=39.99, decimal_places=2)
    image = models.ImageField(upload_to=upload_image_path, null=True)
    featured = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    objects = ProductManager()

    def get_absolute_url(self):
        return "/products/{slug}/".format(slug=self.slug)



def product_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.slug:
        instance.slug=unique_slug_generator(instance)

pre_save.connect(product_pre_save_receiver,sender=product)