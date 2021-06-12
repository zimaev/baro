from django.shortcuts import render, get_object_or_404

from .models import Category, Product, PhotoProduct
from carousel.models import Carousel
from cart.forms import CartAddProductForm




def index(request):
    categories = Category.objects.all()
    carousel_list = Carousel.objects.all()
    products = Product.objects.filter(available=True)[:3]
    context = {
        'category': categories,
        'categories': categories,
        'products': products,
        'carousel_list' : carousel_list 
    }
    return render(request, 'shop/index.html', context)




def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    carousel_list = Carousel.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)

    context = {
        'category': category,
        'categories': categories,
        'products': products,
        'carousel_list' : carousel_list 
    }
    return render(request, 'shop/list.html', context)


def product_detail(request, id, slug):
    categories = Category.objects.all()
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    photos = PhotoProduct.objects.filter(product=product)
    context = {
        'product': product,
        'cart_product_form': cart_product_form,
        'photos':photos,
        'categories': categories
    }
    return render(request, 'shop/single.html', context)
