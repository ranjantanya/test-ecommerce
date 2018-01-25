from django.db import models
from cart.models import Cart
from products.utils import unique_order_id_generator
from decimal import Decimal
from django.db.models.signals import pre_save,post_save
# Create your models here.
ORDER_STATUS_CHOICES={('Created','Created'),('Dispatched','Dispatched'),('Shipped','Shipped'),('Cancelled','Cancelled')}
class Order(models.Model):
    order_id = models.CharField(max_length=20)
    cart = models.OneToOneField(Cart,on_delete=models.CASCADE)
    status = models.CharField(default='Created',choices=ORDER_STATUS_CHOICES,max_length=40)
    shipping_total = models.DecimalField(default =10.00,max_digits=6,decimal_places=2)
    total = models.DecimalField(default=0.00,max_digits=6,decimal_places=2)
    def __str__(self):
        return self.order_id

    def update_total(self):
        cart_total = self.cart.total
        new_total = Decimal(cart_total) + Decimal(self.shipping_total)
        self.total = new_total
        self.save()
        return new_total



def pre_order_save_receiver(sender,instance,*args,**kwargs):
    if not instance.order_id:
        new_order_id = unique_order_id_generator(instance)
        if Order.objects.filter(order_id=new_order_id).exists():
            new_order_id = unique_order_id_generator(instance)
        instance.order_id = new_order_id


pre_save.connect(pre_order_save_receiver,sender=Order)

def post_cart_save_receiver(sender, instance, *args,**kwargs):
    cart_obj = instance
    qs =Order.objects.filter(cart__id=cart_obj.id)
    if qs.count()==1:
        order_obj = qs.first()
        order_obj.update_total()

post_save.connect(post_cart_save_receiver,sender=Cart)

def post_save_order(sender, instance, created, *args,**kwargs):
    if created:
        instance.update_total()

post_save.connect(post_cart_save_receiver,sender=Order)
