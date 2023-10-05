from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
from openpyxl import load_workbook
import pandas as pd

from .models import Category, Product

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    product_list = Product.objects.all()
    context = {"product_list": product_list, "category_list": category_list}
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
    if request.method == "GET":
        print("hello world")
    
    if request.method == "POST":

        # IMPORTING EXCEL
        excel_file = request.FILES["excel_file"]
        wb = load_workbook(excel_file)
        worksheet = wb["Sheet1"]
        excel_data = list()
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))

            excel_data.append(row_data)

            # BEGIN EXTRACTING INFO FROM EXCEL INTO DB
            category_var = row_data[3]
            categoryInstance = Category.objects.get(id=category_var)
            name_var = row_data[0]
            SKU_var = row_data[1]
            desc_var = row_data[2]
            vendor_var = row_data[4]
            price_var = row_data[5]
            specialPrice_var = row_data[6]

            # CREATING THIS OBJECT INTO DB
            Product.objects.create(name= name_var, SKU=SKU_var, description=desc_var, category= categoryInstance, vendor=vendor_var, price = price_var, specialPrice=specialPrice_var)

    return render(request, 'main_page/import_form.html')
