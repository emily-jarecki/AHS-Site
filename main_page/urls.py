from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:category_id>/", views.detail, name="detail"),
    path("product/<int:product_id>/", views.product_detail, name="product_detail"),
    path('import/', views.import_from_excel, name='import_from_excel'),
    path("viewcart/", views.view_cart, name="view_cart"),
]