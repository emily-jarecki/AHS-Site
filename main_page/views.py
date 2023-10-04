from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from openpyxl import load_workbook
import pandas as pd

from .models import Category, Product

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    print(category_list)

    dataframe1 = pd.read_excel(r"C:\Users\E.Jarecki\OneDrive - American Health Services\Desktop\Book1.xlsx")
    df = pd.DataFrame(dataframe1)
    name_list = df['name'].tolist()

    # the entire excel info
    print(df)

    # just the names
    print(name_list)

    context = {'category_list': category_list, 'product_name': name_list}

    return render(request, 'main_page/index.html', context)

def detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    products = category.product_set.all()
    context = {'category': category, 'products': products}
    return render(request, "main_page/detail.html", context)

def product_detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {"product": product}
    return render(request, "main_page/product_detail.html", context)

def import_from_excel(request):
    print(request.method.excel_file)
    if request.method == "GET":
        return render(request, 'main_page/import_form.html')
    if request.method == "POST":
        print(request)
        # excel_file = request.FILES[r"C:\Users\E.Jarecki\OneDrive - American Health Services\Desktop\Book1.xlsx"]
        # wb = load_workbook(excel_file)
        # ws = wb.active
        return render(request, 'main_page/import_form.html')

    #     for row in ws.iter_rows(min_row=7, values_only=True):
    #         name, SKU, description, vendor, price, specialPrice, category_id = row
    #         Product.objects.create(name=name, SKU=SKU, description=description, vendor=vendor, price=price, specialPrice=specialPrice, category_id=category_id)
        
    #     return render(request, 'main_page/import_success.html')
    # else: 
