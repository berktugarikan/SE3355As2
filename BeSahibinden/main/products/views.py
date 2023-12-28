from django.shortcuts import render
from django.views import View

from .models import Product


# Create your views here.

class getAllProducts(View):

    def get(self, request):
        products = Product.objects.all()
        return render(request, 'base.html', {'products': products})

class getDetail(View):
    def get(self, request, product_id):
        product = Product.objects.get(id=product_id)
        return render(request, 'product_detail.html', {'product': product})


class search_product(View):
    def get(self,request):
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = Product.objects.all()

        return render(request, 'search_results.html', {'products': products, 'query': query})