from django.shortcuts import render
from django.http import JsonResponse
import json
import datetime
from .models import * 
from django.contrib.auth import *
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json
import datetime
from django.utils import timezone

def store(request):
	data = cartData(request)

	cartItems = data['cartItems']
	cart = data['cart']
	items = data['items']
	categories = Category.objects.all()

	if(request.GET.get('cat')):
		products = Product.objects.filter(Cate=request.GET.get('cat'))
		cate = Category.objects.get(id=request.GET.get('cat'))
		cateName = cate.Name
	else:
		products = Product.objects.all()
		cateName = "All products"
	context = {'products':products, 'cartItems':cartItems, 'categories':categories, 'cateName':cateName}
	return render(request, 'store/store.html', context)


def cart(request):
	if request.user.is_authenticated:
		data = cartData(request)

		cartItems = data['cartItems']
		cart = data['cart']
		items = data['items']

		context = {'items':items, 'cart':cart, 'cartItems':cartItems}
		return render(request, 'store/cart.html', context)

def checkout(request):
	data = cartData(request)
	
	cartItems = data['cartItems']
	cart = data['cart']
	items = data['items']

	context = {'items':items, 'cart':cart, 'cartItems':cartItems}
	return render(request, 'store/checkout.html', context)

def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)
	
	user = request.user.customer
	product = Product.objects.get(id=productId)
	cart, created = Cart.objects.get_or_create(CustomerID=user)
	cartDetail, created = CartDetail.objects.get_or_create(Cart=cart, ProductID=product)

	if action == 'add':
		cartDetail.Quantity = (cartDetail.Quantity + 1)
	elif action == 'remove':
		cartDetail.Quantity = (cartDetail.Quantity - 1)

	cartDetail.save()

	if cartDetail.Quantity <= 0:
		cartDetail.delete()

	return JsonResponse('Item was added', safe=False)

def processOrder(request):
	if request.user.is_authenticated:
		name = request.POST['name']
		email = request.POST['email']
		address = request.POST['address']
		phone = request.POST['phone']
		user = request.user.customer
		cart = Cart.objects.get(CustomerID=user)

		order = Order(CreatedDate=timezone.now,CustomerID=user,Total=cart.get_cart_total,Status='Submitted',FullName=name,Mail=email,Address=address,Phone=phone)
		order.save()

		orderdetail = OrderDetail()
		for cart in CartDetail.objects.filter(Cart=cart):
			orderdetail = OrderDetail(ProductID=cart.ProductID,OrderID=order,Quantity=cart.Quantity)
			orderdetail.save()
			cart.delete()

	return render(request, 'store/order-success.html', context)


def cartData(request):
	if request.user.is_authenticated:
		user = request.user.customer
		cart, created = Cart.objects.get_or_create(CustomerID=user)
		items = cart.cartdetail_set.all()
		cartItems = cart.get_cart_items
		return {'cartItems':cartItems ,'cart':cart, 'items':items}

	return {'cartItems':0 ,'cart':0, 'items':0}

def loginWeb(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
    	login(request, user)
        # Redirect to a success page.
        
    else:
        # Return an 'invalid login' error message.
        ...
    return HttpResponseRedirect('/')
def signupWeb(request):
    username = request.POST['username']
    password = request.POST['password']
    user = User.objects.create_user(username,None, password)
    user.save()
    customer = Customer(user=user)
    customer.save()
    user = authenticate(username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect('/')
        
    else:
        # Return an 'invalid login' error message.
        ...

def logoutWeb(request):
	logout(request)
	return HttpResponseRedirect('/')

def productview(request):
	data = cartData(request)

	cartItems = data['cartItems']

	categories = Category.objects.all()
	productid = request.GET.get('id')
	product = Product.objects.get(id=productid)

	context = {'product':product, 'cartItems':cartItems, 'categories':categories}
	return render(request, 'store/productview.html', context)