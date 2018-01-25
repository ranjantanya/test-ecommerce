from django.shortcuts import render
from django.views import generic
from .models import product,ProductManager
from cart.models import Cart
# Create your views here.
class ProductListView(generic.ListView):
    queryset = product.objects.all()
    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView,self).get_context_data(*args,**kwargs)
        print(context)
        return context

class ProductDetailView(generic.DetailView):
    model = product


class ProductFeaturedListView(generic.ListView):
    template_name = 'products/product_list.html'
    queryset = product.objects.featured()
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return product.objects.featured()

class ProductFeaturedDetailView(generic.DetailView):
    template_name = 'products/product_detail.html'
    queryset = product.objects.featured()
    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return product.objects.featured()

class ProductDetailSlugView(generic.DetailView):
    template_name = 'products/product_detail.html'
    queryset = product.objects.all()

    def get_context_data(self, *args, **kwargs):
        request=self.request
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        context['cart'] = cart_obj
        return context
