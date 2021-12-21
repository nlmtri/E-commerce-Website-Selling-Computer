from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('adminpage/', views.admin, name="adminpage"),
    path('adminpage/categories', views.categories, name="acategories"),
    path('adminpage/users', views.users, name="ausers"),
    path('adminpage/products', views.products, name="aproducts"),
    path('adminpage/orders', views.orders, name="aorders"),
]
