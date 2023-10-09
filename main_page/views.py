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
    #pass another value send over that value in post data
    product = get_object_or_404(Product, pk=product_id)

    # receiving data from the views
    if request.method == "POST":
        if 'myCart' in request.session:
            print("It exists")
        else: 
            print("I have to create a my_cart")
            request.session["myCart"] = []

        menu=[]
        menu.append(request.session['myCart'])

        flattened = []

        for item in menu:
            if isinstance(item, list):
                flattened.extend(item)
                flattened.append(product_id)
            else:
                flattened.append(item)
                flattened.append(product_id)

        print(flattened)

        # creating a session
        request.session["myCart"] = flattened
        print("The new session: ", request.session['myCart'])
        # del request.session['cart']

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


def view_cart(request):
    cart_list = request.session['myCart']
    product_in_cart_list = []

    for item in cart_list:
        product_in_cart = Product.objects.filter(id=item)[0]
        product_in_cart_list.append(product_in_cart)

    for p in product_in_cart_list:
        print(p)

    context = {"cart_list": cart_list, "product_in_cart_list": product_in_cart_list, "product_in_cart" : product_in_cart}
    return render(request, 'main_page/viewcart.html', context)
