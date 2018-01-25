"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from cart.views import cart_home
from products.views import ProductFeaturedListView,ProductFeaturedDetailView
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.home_page,name='home_page'),
    url(r'^contact/$',views.contact_page,name='contact_page'),
    url(r'^login/$',views.login_page,name='login_page'),
    url(r'^logout/$',views.logout_page,name='logout_page'),
    url(r'^register/$', views.register_page, name='register_page'),
    url(r'^products/',include("products.urls")),
    url(r'^search/', include("search.urls", namespace="search")),
    # url(r'^products/$', ProductListView.as_view(), name='product_list'),
    # # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    # url(r'^products/(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='product_slug_detail'),
    url(r'^featured/$', ProductFeaturedListView.as_view(), name='product_featured_list'),
    url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view(), name='product_featured_detail'),
    url(r'^cart/',include("cart.urls", namespace="cart")),
]

if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root= settings.STATIC_ROOT)
    urlpatterns+=static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)