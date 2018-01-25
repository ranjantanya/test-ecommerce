from django.contrib import admin
from .models import product
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','slug']
    class Meta:
        model = product
admin.site.register(product,ProductAdmin)