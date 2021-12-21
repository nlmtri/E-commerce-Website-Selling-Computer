from django.urls import path
from . import views
from django.conf.urls import include

urlpatterns = [
    path('', views.store, name="store"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('login/', views.loginWeb, name="login"),
    path('signup/', views.signupWeb, name="signup"),
    path('logout/', views.logoutWeb, name="logout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]
