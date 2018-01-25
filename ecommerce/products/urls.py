
from django.urls import path
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from .views import ProductListView,ProductDetailSlugView
from . import views

urlpatterns = [

    url(r'^$', ProductListView.as_view(), name='product_list'),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='product_slug_detail'),

]
