from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
User = settings.AUTH_USER_MODEL
# Create your models here.
class BillingProfile(models.Model):
    user = models.OneToOneField(User,blank=True,null=True)
    email = models.EmailField()
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.email

def user_created_receiver(sender, instance,created, *args,**kwargs):
    if created and instance.email:
        BillingProfile.objects.get_or_create(user=instance,email=instance.email)

post_save.connect(user_created_receiver,sender=User)