from django.shortcuts import render
from django.views import generic
from django.http import request
from products.models import product
from django.db.models import Q
# Create your views here.
class SearchProductView(generic.ListView):
    template_name = "search/view.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        query = request.GET.get('q',None)
        if query is not None:
            return product.objects.searched(query)
        return product.objects.featured()