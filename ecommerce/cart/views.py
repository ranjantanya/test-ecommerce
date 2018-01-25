from django.shortcuts import render,redirect
from django.views import generic
from .models import Cart
from orders.models import Order
from products.models import product
from billing.models import BillingProfile
# Create your views here.
#
def cart_create(user=None):
    cart_obj = Cart.objects.create(user=None)
    return cart_obj

def cart_home(request):
    # request.session['user'] = request.user.username
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    return render(request,"cart/home.html",{"cart":cart_obj})

def cart_update(request):
    product_id = request.POST.get('product_id')
    if product_id is not None:
        try:
            product_obj = product.objects.get(id=product_id)
        except product.DoesNotExist:
            print('Error')
            return redirect("cart:home")
        cart_obj,new_obj = Cart.objects.new_or_get(request)
        if product_obj in cart_obj.products.all():
            cart_obj.products.remove(product_obj)
        else:
            cart_obj.products.add(product_obj)
        cart_obj.save()
        request.session['cart_items'] = cart_obj.products.count()
    return redirect("cart:home")


def checkout_home(request):
    cart_obj,new_obj = Cart.objects.new_or_get(request)
    order_obj = None

    if new_obj or cart_obj.products.count() == 0:
        return redirect("cart:home")
    else:

        if request.user.is_authenticated:
            billing_profile =BillingProfile.objects.filter(User=request.user)
            context={"billingprof":billing_profile}

        order_obj,new_order_obj = Order.objects.get_or_create(cart=cart_obj)
        if new_order_obj:
            order_obj.update_total()
        context+= {"cart": cart_obj, "order": order_obj}
    return render(request,"cart/checkout.html",context)