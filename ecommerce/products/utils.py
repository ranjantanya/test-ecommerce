import random
import string
from django.utils.text import slugify

def random_string_generator(size=10,chars=string.ascii_lowercase+string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def unique_slug_generator(instance, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    else:
        slug = slugify(instance.title)
    Klass = instance.__class__
    qs_exists = Klass.objects.filter(slug__iexact=slug).exists()
    if qs_exists:
        new_slug= {0}-{1}.format(slug,random_string_generator(size=4))
        return unique_slug_generator(instance, new_slug=new_slug)
    return slug

def unique_order_id_generator(instance):
    new_order_id= random_string_generator(size=5)
    return new_order_id