from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from django.template import loader
import openpyxl
from openpyxl import load_workbook
import pandas as pd

from .models import Category, Product

# Create your views here.
def index(request):
    category_list = Category.objects.all()
    print(category_list)

    # HARDCODE LOCATION INTO INDEX PAGE - NOT IDEAL 
    dataframe1 = pd.read_excel(r"C:\Users\E.Jarecki\OneDrive - American Health Services\Desktop\Book1.xlsx")
    df = pd.DataFrame(dataframe1)
    name_list = df['name'].tolist()

    # ENTIRE EXCEL INFO
    print(df)

    # JUST THE NAMES COLUMN
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
    if request.method == "GET":
        print("hello world")
        return render(request, 'main_page/import_form.html')
    
    if request.method == "POST":

        # TYPE OF REQUEST
        print(request)
        excel_file = request.FILES["excel_file"]

        # THE TITLE OF EXCEL FILE
        print(excel_file)
        wb = load_workbook(excel_file)

        #  CRAZY: <openpyxl.workbook.workbook.Workbook object at 0x000001A8590C2D50>
        print("WB: ", wb)
        
        # GETTING SHEET1 -  as a precaution
        worksheet = wb["Sheet1"]

        # <Worksheet "Sheet1">
        print("Worksheet: ", worksheet)

        # WHATEVER VALUE IS IN A1 
        # ONLY A SINGLE VALUE
        print(worksheet["A1"].value)

        excel_data = list()

        # iterating over the rows and getting value from each cell in row
        for row in worksheet.iter_rows():
            row_data = list()
            for cell in row:
                row_data.append(str(cell.value))
            excel_data.append(row_data)

            # ALL ROWS 
            print(row_data)
        
        return render(request, 'main_page/import_form.html', {"excel_data":excel_data})