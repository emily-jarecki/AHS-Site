from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
import pandas as pd

from .models import Category, Product

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    print(category_list)

    dataframe1 = pd.read_excel(r"C:\Users\E.Jarecki\OneDrive - American Health Services\Desktop\Book1.xlsx")
    df = pd.DataFrame(dataframe1)
    name_list = df['Name'].tolist()
    print(name_list)

    context = {'category_list': category_list, 'product_name': name_list}
    
    return render(request, 'main_page/index.html', context)

def detail(request, category_id):
    # category = Category.objects.get(pk=category_id)
    category = get_object_or_404(Category, pk=category_id)
    products = category.product_set.all()
    context = {'category': category, 'products': products}
    return render(request, "main_page/detail.html", context)

def product_detail(request, product_id):
    # product = Product.objects.get(pk=product_id)
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "main_page/product_detail.html", context)
