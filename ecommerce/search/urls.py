
from django.urls import path
from django.conf.urls import url
from .views import SearchProductView
from django.conf import settings
from django.conf.urls.static import static
from products.views import ProductListView
from . import views
app_name='search'
urlpatterns = [

    url(r'^$', SearchProductView.as_view(), name='query'),

]
