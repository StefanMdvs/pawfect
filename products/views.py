from django.shortcuts import render, get_object_or_404
from .models import Product

def all_products(request):
    """
    View to return all products, sorting and search queries
    """

    products = Product.objects.all()

    context = {
        'products': products,
    }
    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """
    View to show details about a product
    """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }
    return render(request, 'products/product_detail.html', context)