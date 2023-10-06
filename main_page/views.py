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

#prod_id, qty
def product_detail(request, product_id):
    #pass another value send over that value in post data
    product = get_object_or_404(Product, pk=product_id)

    # receiving data from the views
    if request.method == "POST":



        #take the id from add to cart button
        #then search the instace
        #add the instance to the session list
        #u
        ###########

        # intace = [instance , instace 2] 


        # request.session['my_cart'] = product_id
        # print(request.session['my_cart'])

        menu=[]
        menu.append(request.session['cart'])
        menu.append(product_id)
        print(menu)

        # # creating a session
        request.session["cart"] = menu
        print("DA NEW MENU: ", request.session['cart'])

        # request.sesion= instace
        # menu = []
        # menu.append("string test")
        # request.session["menu"] = menu
        # varList2 = ["Geeks2", "for", "Geeks"]
        
        # request.session["list3"] = varList2
        # print(request.session["list3"])
        # print(request.session["menu"])
        
        # listOfCartItems = []

        # SECOND WAY TO DO IT
        # for key in request.session.keys():
        #     print("key:=>" + str(request.session[key]))


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
